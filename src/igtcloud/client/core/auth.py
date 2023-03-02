import base64
import json
import mmap
import os
import signal
import sys
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone, timedelta
from getpass import getpass
from http import cookies
from threading import Lock, Timer
from time import sleep
from urllib.parse import urlparse, urljoin

import requests
import logging

from jwt import JWT, jwk_from_pem
from requests import RequestException
from tenacity import retry, wait_exponential, stop_after_delay, retry_if_exception_type

logger = logging.getLogger(__name__)


@contextmanager
def smart_auth(domain, username=None, key=None):
    url = urlparse(domain)
    if not url.scheme:
        url = urlparse('https://' + domain)
    domain = url.geturl()
    auth = None
    try:
        try_auth = AuthHandler()
        if try_auth.domain == domain and try_auth.is_valid and (not username or try_auth.username == username):
            auth = try_auth
    except RuntimeError:
        pass
    try:
        if auth is None:
            with AuthRefresher(domain=domain, username=username, key=key) as auth:
                yield auth
        else:
            yield auth
    finally:
        auth.close()


def _get_mmap_filename():
    return os.environ.get('CLOUD_TOKEN_MMAP', os.path.join(tempfile.gettempdir(), 'igtcloud_auth_mmap'))


class AuthHandler:
    def __init__(self, filename=None):
        self._mmap_filename = filename or _get_mmap_filename()
        self._token = None
        self._mmap = None
        self._file = None
        self._cached_token = dict()

    @property
    def jwt_token(self):
        token = self._read_token()
        return token.get("jwt")

    @property
    def csrf_token(self):
        token = self._read_token()
        return token.get("csrf")

    @property
    def access_token(self):
        return self._jwt_data.get("access_token")

    @property
    def is_valid(self):
        now = datetime.now().timestamp()
        return self._jwt_data.get("exp") > now

    @property
    def domain(self):
        token = self._read_token()
        return token.get("domain")

    @property
    def username(self):
        token = self._read_token()
        return token.get("sub")

    @property
    def uid(self):
        return self._jwt_data.get('uid')

    @property
    def _jwt_data(self):
        token = self._read_token()
        return token.get("jwt_data", {})

    def _read_token(self):
        if self._mmap is None:
            if not os.path.exists(self._mmap_filename):
                raise RuntimeError("IGT Cloud auth file doesn't exist.\nPlease login using `igtcloud login`")
            try:
                self._file = open(self._mmap_filename, 'r+b', 0)
                if sys.platform != "win32":
                    self._mmap = mmap.mmap(self._file.fileno(), 0, mmap.MAP_SHARED, mmap.ACCESS_READ)
                else:
                    self._mmap = mmap.mmap(self._file.fileno(), 0, access=mmap.ACCESS_READ)
            except Exception:
                raise RuntimeError('Error opening IGT Cloud auth file {}'.format(self._mmap_filename))
        self._mmap.seek(0)
        try:
            data = self._mmap.readline().decode('utf-8').strip().strip('\x00')
            data = base64.b64decode(data)
            self._cached_token = json.loads(data)
        except Exception:
            logger.error("Error retrieving/decoding token")
        return self._cached_token

    def __del__(self):
        self.close()

    def close(self):
        if self._mmap is not None:
            self._mmap.close()
            self._file.close()


class AuthRefresher:
    def __init__(self, **kwargs):
        self._filename = _get_mmap_filename()
        self._unique = kwargs.pop('unique', False)

        self._domain = None
        self._host = None
        self._token_data = dict()
        self._file = None
        self._m = None

        self._authhandler = None

        self._rt = Periodic(-1, self._refresh_token, autostart=False)
        self._running = False

        signals = [signal.SIGABRT, signal.SIGINT, signal.SIGTERM]
        if sys.platform != "win32":
            signals.append(signal.SIGHUP)
        for signum in signals:
            signal.signal(signum, self._signal_handler)

        self._start_kwargs = kwargs

    def __enter__(self):
        self._unique = True
        self.start(blocking=False, **self._start_kwargs)
        self._authhandler = AuthHandler(filename=self._filename)
        return self._authhandler

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def _save_data(self):
        self._rt.interval = int(self._token_data['expires_in']) - 180
        data = {k: v for k, v in self._token_data.items() if
                k in ['sub', 'jwt', 'jwt_data', 'csrf']}

        # Add domain
        data['domain'] = self._domain

        data = base64.b64encode(json.dumps(data).encode('utf-8'))
        if self._m:
            self._m.seek(0)
            self._m.write(data)
            self._m.flush()

    def _oauth_login(self, username, password):

        data = {'grantType': 'password',
                'username': username,
                'password': password}
        self._token_data = self._oauth_token(data, 'login')
        self._token_data["csrf"] = self._token_data["CSRFToken"]  # Copy csrf, is only valid on logon, not refresh

    def _oauth_login_jwt(self, sub, key, aud=None):
        if aud is None:
            resp = requests.get(urljoin(self._domain, '/api/auth/login/$aud'))
            if resp.ok:
                aud = resp.json()
            else:
                logger.error(resp.text)
                resp.raise_for_status()
        payload = dict(
            aud=[aud],
            iss=sub,
            sub=sub,
            exp=int((datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(hours=1)).timestamp()))

        jwt = JWT()
        signing_key = jwk_from_pem(key.encode())
        assertion = jwt.encode(payload, signing_key, 'RS256')

        data = {'grantType': 'jwt-key',
                'assertion': assertion,
                'hospitalOrgId': ""
                }
        self._token_data = self._oauth_token(data, 'login')
        self._token_data["csrf"] = self._token_data["CSRFToken"]  # Copy csrf, is only valid on logon, not refresh
        self._token_data["key"] = key  # Store key to allow re-login
        self._token_data["aud"] = aud  # Store aud to allow re-login

    def _oauth_token(self, data, action='login'):
        url = urljoin(self._domain, f'/api/auth/{action}')
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json'}
        if action == 'refresh':
            headers['X-JWT'] = self._token_data['jwt']
            headers['X-CSRF-TOKEN'] = self._token_data['csrf']

        resp = requests.post(url, json=data, headers=headers)
        if resp.ok:
            data = resp.json()
            c = resp.headers['Set-Cookie']
            cookie = cookies.SimpleCookie()
            cookie.load(c)
            data["jwt"] = f"{cookie['jwt_header_payload'].value}.{cookie['jwt_signature'].value}"
            data["expires_in"] = float(cookie['jwt_header_payload']['max-age'])
            jwt_payload = data["jwt"].split(".")[1]
            jwt_payload += '=' * (-len(jwt_payload) % 4)  # pad payload
            data["jwt_data"] = json.loads(base64.b64decode(jwt_payload))
            return data
        else:
            logger.error(resp.text)
            resp.raise_for_status()

    def _login(self, username=None, key=None):
        if self._token_data is None or self._token_data.get('refresh_token') is None:
            logger.info("Login to IGT Cloud ({})".format(self._host))

            if username and key:
                try:
                    self._oauth_login_jwt(username, key)
                except:
                    raise RuntimeError('Error during login')
            else:
                username = username or os.environ.get('CLOUD_USERNAME') or input("Username: ")
                password = getpass('{}@{}\'s password: '.format(username, self._host))

                try:
                    self._oauth_login(username, password)
                except:
                    raise RuntimeError('Error during login')
        else:
            try:
                self._oauth_refresh_token()
            except:
                raise RuntimeError('Error during login using refresh token')

        logger.info(
            'Logged in as: {sub}'.format(sub=self._token_data.get('sub', None)))
        self._save_data()

    def _logout(self):
        logger.info("Logout...")
        url = urljoin(self._domain, '/api/auth/logout')
        headers = {'X-JWT': self._token_data['jwt']}
        resp = requests.post(url, {}, headers=headers)
        return resp.ok

    def _refresh_token(self):
        logger.info('Refreshing token')
        try:
            if self._token_data.get('jwt_data', {}).get('refresh_token') is not None:
                csrf = self._token_data.get('csrf')
                self._oauth_refresh_token()

                self._token_data['csrf'] = csrf
            elif self._token_data.get('key') is not None:
                self._oauth_login_jwt(self._token_data.get('sub'), self._token_data.get('key'),
                                      self._token_data.get('aud'))
            else:
                raise RuntimeError()
            self._save_data()
        except:
            logger.error("Error during refresh")
            self.stop()

    @retry(stop=(stop_after_delay(180)), wait=wait_exponential(),
           retry=retry_if_exception_type(RequestException), reraise=True)
    def _oauth_refresh_token(self):
        self._token_data = self._oauth_token(None, 'refresh')

    def _signal_handler(self, signum, frame):
        logger.debug('Signal handler called with signal %s', signal.strsignal(signum))
        self.stop()
        if signum == signal.SIGINT:
            signal.default_int_handler(signum, frame)

    def stop(self):
        if self._running:
            if self._authhandler:
                try:
                    self._authhandler.close()
                except Exception:
                    pass
            self._rt.stop()
            try:
                self._m.close()
                self._m = None
                self._file.close()
                self._file = None
                os.remove(self._filename)
            except:
                logger.debug("Error during stop")
            try:
                self._logout()
            except:
                logger.debug("Error during logout")
            self._running = False
            logger.info("Stopped IGT Cloud authentication handler")

    def start(self, domain=None, username=None, key=None, blocking=True):
        self._setup_mmap()
        try:
            logger.info("Starting IGT Cloud authentication handler...")
            self._running = True

            domain = domain or os.environ.get('CLOUD_DOMAIN') or input("Provide domain: ")
            if not domain:
                raise RuntimeError("Domain not provided")

            url = urlparse(domain)
            if not url.scheme:
                url = urlparse('https://' + domain)
            self._domain = url.geturl()
            self._host = url.netloc

            self._login(username=username, key=key)
            self._rt.start()
            while blocking and self._running:
                sleep(1)
        except (InterruptedError, KeyboardInterrupt):
            pass

    def _setup_mmap(self):
        if self._file is None or self._m is None:
            if self._unique:
                fd, self._filename = tempfile.mkstemp(prefix=os.path.basename(self._filename),
                                                      dir=os.path.dirname(self._filename))
                self._file = open(fd, 'w+b', 0)
            else:
                os.makedirs(os.path.dirname(self._filename), exist_ok=True)
                self._file = open(self._filename, 'w+b', 0)

            self._file.write(b'\x00' * 5 * mmap.PAGESIZE)
            self._file.flush()
            if sys.platform != "win32":
                self._m = mmap.mmap(self._file.fileno(), 5 * mmap.PAGESIZE, mmap.MAP_SHARED, mmap.ACCESS_WRITE)
            else:
                self._m = mmap.mmap(self._file.fileno(), 5 * mmap.PAGESIZE, access=mmap.ACCESS_WRITE)


class Periodic(object):
    """
    A periodic task running in threading.Timers
    """

    def __init__(self, interval, function, *args, **kwargs):
        self._lock = Lock()
        self._timer = None
        self.function = function
        self.interval = interval
        self.args = args
        self.kwargs = kwargs
        self._stopped = True
        if kwargs.pop('autostart', True):
            self.start()

    def start(self, from_run=False):
        self._lock.acquire()
        if from_run or self._stopped:
            self._stopped = False
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self._lock.release()

    def _run(self):
        self.function(*self.args, **self.kwargs)
        self.start(from_run=True)

    def stop(self):
        self._lock.acquire()
        self._stopped = True
        if self._timer:
            self._timer.cancel()
        self._lock.release()
