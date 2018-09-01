from setuptools import setup, find_packages

setup (
    name = 'peakweb',
    version='0.1.0',
    description='Peak Web UI',
    url='https://github.com/peak-oss/peakweb',
    author='Peak Development Team',
    author_email='dev@peak-oss.tech',
    keywords='peak api testing containers docker',
    include_package_data=True,
    packages=find_packages()
)
