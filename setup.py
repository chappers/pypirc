#!/usr/bin/env python
"""PyPiRC"""
__author__ = 'Greg Albrecht <gba@splunk.com>'
__copyright__ = 'Copyright 2012 Splunk, Inc.'
__license__ = 'Apache License 2.0'


import setuptools


def read_readme():
    """Reads in README file for use in setuptools."""
    with open('README.rst') as rmf:
        rmf.read()


setuptools.setup(
    name='pypirc-chappers',
    version='1.0.8',
    description='PyPiRC: .pypirc Manager',
    long_description=read_readme(),
    author='Greg Albrecht',
    author_email='gba@splunk.com',
    maintainer="Chapman Siu",
    maintainer_email="chapm0n.siu@gmail.com",
    url='https://github.com/chappers/pypirc',
    license='Apache License 2.0',
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    install_requires=['future'],
    setup_requires=['nose'],
    tests_require=['nose', 'mock', 'coverage'],
    test_suite='tests',
    entry_points={'console_scripts': ['pypirc = pypirc.cmd:main']}
)
