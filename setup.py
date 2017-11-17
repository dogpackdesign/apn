#!/usr/bin/env python
import os

from setuptools import setup, find_packages

from apn import __version__


def read(*names):
    values = dict()
    extensions = ['.txt', '.rst']
    for name in names:
        value = ''
        for extension in extensions:
            filename = name + extension
            if os.path.isfile(filename):
                value = open(name + extension).read()
                break
        values[name] = value
    return values


long_description = """
%(README)s

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')

setup(
    name='apn',
    version=__version__,
    author="Eric Proulx",
    author_email="eric@ericproulx.com",
    keywords="apn real estate format",
    url="https://github.com/dogpackdesign/apn-formats",
    description="Accessor Parcel Number format lookup",
    long_description=long_description,
    license="MIT",
    packages=find_packages(),
    package_data={'apn': ['data/*.pkl']},
    package_dir={'apn':'apn'},
    entry_points={
        'console_scripts': ['apn = apn.cli.apn:runner']
    },
    platforms=['any'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'python-Levenshtein',
        'fuzzywuzzy'
    ]
)
