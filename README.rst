apn
====================================================

Validate or lookup Assessor's Parcel Number (APN) formats for any given state/county in the United States.
----------------------------------------------------------------------------------------------------------
Lookup or validate an APN format for
a given county and/or state.

.. image:: https://travis-ci.org/dogpackdesign/apn.svg?branch=master
    :target: https://travis-ci.org/profile/dogpackdesign

Installation
------------

::

    pip install apn

Usage
-----

::

    usage: apn.py [-h] [-s STATE] [-c COUNTY] [-l] [-v]

    Look up APN format by State and/or County

    optional arguments:
      -h, --help            show this help message and exit
      -s STATE, --state STATE
                            US state to lookup APN format
      -c COUNTY, --county COUNTY
                            by specific county
      -l, --list            list all APNs
      -v, --version         current version

More examples of how to use in command line or in code

::

    $ apn -s WA -c King
    > import apn
    > results = apn.lookup('WA','King)

Authors
-------

- **Eric Proulx** - *Owner* - `Website <http://www.ericproulx.com/>`__
- **Ken Harmon** - *Owner* - `Website <https://kenharmon.net/>`__

Notes
-----

- Works with Python2 and Python3
- apn uses pkl files to store APN, state data

Development
-----------

- Clone repo
- Run ``python -m apn.cli.apn`` for console
- Changes/improvements welcome!
- To add data, please edit the apn.db Sqlite db and then run ``python build.py``
