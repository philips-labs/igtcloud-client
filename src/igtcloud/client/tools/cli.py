import logging
import click

from . import logger
from .common import TqdmLoggingHandler

logging.basicConfig(level=logging.INFO, handlers=[TqdmLoggingHandler()])


@click.group()
def cli():
    """Philips Interventional Cloud CLI"""
    pass


@click.command(short_help="Download data from Philips Interventional Cloud")
@click.argument('target_folder')
@click.argument('project')
@click.argument('institute', required=False, default='*')
@click.argument('environment', required=False, default='PROD', type=click.Choice(['PROD', 'TEST'],
                                                                                 case_sensitive=False))
@click.option('--domain', default=None, help='Overwrites the environment setting')
@click.option('--user', default=None, help='Username')
@click.option('--ext', default=None, help='filter on specific file extension (i.e.: \'.txt\')')
@click.option('--start', default=None, help='start date (YYYY-MM-DD) of date range filter. Default value is 1900-01-01.')
@click.option('--end', default=None, help='end date (YYYY-MM-DD) of date range filter. Default value is 9999-12-31.')
@click.option('--category', default=['files'], multiple=True, type=click.Choice(['files', 'dicom', 'annotations'],
                                                                                case_sensitive=False),
              help='Categories of files to download')
@click.option('--debug', flag_value=True, help='Enable debug logging')
def download(target_folder, project, institute, environment, domain, user, ext, start, end, category, debug):
    """Download data from Philips Interventional Cloud.

    \b
    This tool will download all files from INSTITUTE in project PROJECT to TARGET_FOLDER.
    the folder structure will be TARGET_FOLDER / INSTITUTE / <patient study name> / <files and folders"""
    if debug:
        logging.getLogger('igtcloud.client').setLevel(logging.DEBUG)

    from igtcloud.client.core.auth import smart_auth
    from igtcloud.client.services import set_auth
    from igtcloud.client.tools.common import filter_by_study_date, filter_by_ext
    from igtcloud.client.tools.download_institute import download_institutes

    if institute == "*":
        institute = None

    domain = _get_domain(domain, environment)
    with smart_auth(domain, username=user) as auth:
        set_auth(auth)
        logger.info(f"Using url: {auth.domain}")
        download_institutes(project, institute, target_folder, categories=category, files_filter=filter_by_ext(ext),
                            studies_filter=filter_by_study_date(start, end))


@click.command(short_help="List data from Philips Interventional Cloud in CSV file")
@click.argument('target_folder')
@click.argument('project')
@click.argument('institute', required=False, default='*')
@click.argument('environment', required=False, default='PROD', type=click.Choice(['PROD', 'TEST'],
                                                                                 case_sensitive=False))
@click.option('--domain', default=None, help='Overwrites the environment setting')
@click.option('--user', default=None, help='Username')
@click.option('--ext', default=None, help='filter on specific file extension (i.e.: \'.txt\')')
@click.option('--start', default=None, help='start date (YYYY-MM-DD) of date range filter. Default value is 1900-01-01.')
@click.option('--end', default=None, help='end date (YYYY-MM-DD) of date range filter. Default value is 9999-12-31.')
@click.option('--debug', flag_value=True, help='Enable debug logging')
@click.option('--files', flag_value=True, help='Output all files under patient studies')
def csv(target_folder, project, institute, environment, domain, user, ext, start, end, debug, files):
    """List data from Philips Interventional Cloud in CSV file.

    This tool will export all studies/files from INSTITUTE (or all institutes) in project PROJECT to
    TARGET_FOLDER/cloud_??.csv
    """
    if debug:
        logging.getLogger('igtcloud.client').setLevel(logging.DEBUG)

    from igtcloud.client.core.auth import smart_auth
    from igtcloud.client.services import set_auth
    from igtcloud.client.tools.common import filter_by_study_date, filter_by_ext
    from igtcloud.client.tools.list_project import list_project

    if institute == "*":
        institute = None

    domain = _get_domain(domain, environment)
    with smart_auth(domain, username=user) as auth:
        set_auth(auth)
        logger.info(f"Using url: {auth.domain}")
        list_project(project, target_folder, institute_name=institute, list_files=files,
                     files_filter=filter_by_ext(ext), studies_filter=filter_by_study_date(start, end))


def _get_domain(domain, environment):
    if domain is None:
        if environment == 'PROD':
            domain = "igt-web.eu1.phsdp.com"
        elif environment == 'TEST':
            domain = "igt-web-test.eu1.phsdp.com"
        else:
            raise RuntimeError("Unsupported environment")
    return domain


@click.command(short_help="Upload data to Philips Interventional Cloud")
@click.argument('local_folder')
@click.argument('project')
@click.argument('institute', required=False, default='*')
@click.argument('environment', required=False, default='PROD', type=click.Choice(['PROD', 'TEST'],
                                                                                 case_sensitive=False))
@click.option('--domain', default=None, help='Overwrites the environment setting')
@click.option('--user', default=None, help='Username')
@click.option('--submit', flag_value=True, help='Set electronic record state to submitted state')
@click.option('--debug', flag_value=True, help='Enable debug logging')
@click.option('--concurrent-studies', type=int, default=None, help='Maximum number of concurrent studies upload')
@click.option('--concurrent-files', type=int, default=None, help='Maximum number of concurrent files upload per study')
def upload(local_folder, project, institute, environment, domain, user, submit, debug, concurrent_studies,
           concurrent_files):
    """Upload data to Philips Interventional Cloud.

    \b
    This tool will upload all files in LOCAL_FOLDER to project PROJECT.
    the folder structure should be LOCAL_FOLDER / INSTITUTE / <patient study name> / <files and folders"""
    if debug:
        logging.getLogger('igtcloud.client').setLevel(logging.DEBUG)

    domain = _get_domain(domain, environment)

    from igtcloud.client.core.auth import smart_auth
    from igtcloud.client.services import set_auth
    from igtcloud.client.tools.upload_project import upload_project

    if institute == "*":
        institute = None

    with smart_auth(domain, username=user) as auth:
        set_auth(auth)
        logger.info(f"Using url: {auth.domain}")
        upload_project(local_folder, project, institute, submit, concurrent_studies, concurrent_files)


@click.command(short_help="Login to Philips Interventional Cloud")
@click.option('-d', '--domain', default=None, type=str)
@click.option('-u', '--user', default=None, type=str)
def login(domain, user):
    from igtcloud.client.core.auth import AuthRefresher
    auth_refresher = AuthRefresher()
    auth_refresher.start(domain=domain, username=user)


@click.command('get-token', short_help="Get token for Philips Interventional Cloud")
@click.option('--type', '-t', 'type_', default='jwt', required=False, type=click.Choice(['jwt', 'access', 'csrf'],
                                                                                        case_sensitive=False))
def get_token(type_):
    from igtcloud.client.core.auth import AuthHandler
    auth_handler = AuthHandler()
    if type_ == 'jwt':
        print(auth_handler.jwt_token)
    elif type_ == 'csrf':
        print(auth_handler.csrf_token)
    elif type_ == 'access':
        print(auth_handler.access_token)
    else:
        print('ERROR')


@click.command(short_help="Print version of this tool")
def version():
    from igtcloud.client import __version__
    print(__version__)


@click.command(short_help="Upgrade this tool to a new version")
@click.argument('package_version', required=False, default=None)
def upgrade(package_version):
    from igtcloud.client import __version__, __source__
    if package_version is None:
        import requests
        resp = requests.get(f'{__source__}/releases/latest', allow_redirects=False)
        if resp.status_code == 302:
            redirect_url = resp.headers['Location']
            tag_prefix = '/tag/'
            ix = redirect_url.index(tag_prefix)
            if ix > 0:
                package_version = redirect_url[ix + len(tag_prefix):]
                if __version__ == package_version[1:]:
                    print(f"Already at latest version: {package_version}")
                    return
    if package_version is None:
        print("Cannot determine version")
        return
    import subprocess
    import sys
    subprocess.Popen([sys.executable, '-m', 'pip', 'install', '--upgrade', f'git+{__source__}@{package_version}'])


cli.add_command(version)
cli.add_command(login)
cli.add_command(get_token)
cli.add_command(download)
cli.add_command(upload)
cli.add_command(csv)
cli.add_command(upgrade)
