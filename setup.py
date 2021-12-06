"""
distutils/setuptools install script.
"""

from setuptools import setup, find_namespace_packages


def dev_scheme(version):
    time_format = "%Y%m%d"
    # If branch is dev(elop), use versioning: X.Y.devZ
    # For other branches use: X.Y.devZ+commitSHA
    # in both cases a datetime is appended if repo is dirty
    dev_branches = ['dev', 'develop', 'master']
    if version.exact or version.node is None or version.branch in dev_branches:
        return version.format_choice("",
                                     "+d{time:{time_format}}",
                                     time_format=time_format)
    else:
        return version.format_choice("+{node}",
                                     "+{node}.d{time:{time_format}}",
                                     time_format=time_format)

requires = []
requirements_files = ['requirements.txt']
for file in requirements_files:
    with open(file, mode='r') as f:
        for line in f:
            if not line.startswith('-'):
                line = line.strip()
                if line:
                    requires.append(line)

setup(
    name='igtcloudclient',
    use_scm_version={'write_to': 'src/igtcloud/client/__version__.py', 'local_scheme': dev_scheme},
    author='Koen de Laat (Philips)',
    license="Apache License 2.0",
    author_email='koen.de.laat@philips.com',
    url='https://www.philips.com',
    description='IGT Cloud client',
    package_dir={"": "src"},
    packages=find_namespace_packages(include=['igtcloud.*'], where="src"),
    install_requires=requires,
    scripts=['scripts/igtcloud'],
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
)
