from setuptools import setup, find_packages
from peakweb import run

setup (
    name = 'peakweb',
    version='0.1.0',
    description='Peak Web UI',
    url='https://github.com/peak-oss/peakweb',
    author='Peak Development Team',
    author_email='dev@peak-oss.tech',
    keywords='peak api testing containers docker',
    entry_points = {
        'console_scripts': [
            'peakweb = peakweb.run:main',
        ],
    },
    include_package_data=True,
    packages=find_packages(),
    install_requires=['flask==0.12.2','flask-wtf','requests',
                      'subprocess32', 'gunicorn']
)
