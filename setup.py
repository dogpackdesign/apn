#!/usr/bin/env python

from setuptools import setup, find_packages

from apn import __version__

long_description = open('README.rst').read()

setup(
    name='apn',
    version=__version__,
    author="Eric Proulx",
    author_email="eric@ericproulx.com",
    url="https://github.com/dogpackdesign/apn-formats",
    description="Accessor Parcel Number format lookup",
    long_description=long_description,
    license="MIT",
    packages=find_packages(),
    package_data={'apn': ['data/*.pkl']},
    entry_points={
        'console_scripts': ['apn = apn.cli.apn:runner']
    },
    platforms=['any'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
