import os
import pickle
import re
import sqlite3

import pkg_resources

PWD = os.path.abspath(os.path.dirname(__file__))


def dict_factory(cursor, row):
    return dict((col[0], row[idx]) for idx, col in enumerate(cursor.description))


def validate_regex(raw_regex):
    try:
        re.compile(raw_regex)
        return True
    except re.error:
        return False


def pickle_data():
    db_path = os.path.abspath(os.path.join(PWD, 'apn.db'))
    conn = sqlite3.connect(db_path)
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM apn')
    apns = []
    for row in cursor:
        if validate_regex(row.get('apn_regex')):
            apns.append(row)
    states = []
    state_abbrev = []
    cursor.execute('SELECT * FROM states')
    for row in cursor:
        states.append(row.get('name'))
        state_abbrev.append(row.get('abbrev'))
    apn_pickle_path = pkg_resources.resource_filename('apn', 'data/apn.pkl')
    state_pickle_path = pkg_resources.resource_filename('apn', 'data/state.pkl')
    abbrev_pickle_path = pkg_resources.resource_filename('apn', 'data/abbrev.pkl')

    with open(apn_pickle_path, 'wb') as apn_pickle:
        pickle.dump(apns, apn_pickle, protocol=2)

    with open(state_pickle_path, 'wb') as state_pickle:
        pickle.dump(states, state_pickle, protocol=2)

    with open(abbrev_pickle_path, 'wb') as abbrev_pickle:
        pickle.dump(state_abbrev, abbrev_pickle, protocol=2)


def build():
    pickle_data()


if __name__ == '__main__':
    build()
