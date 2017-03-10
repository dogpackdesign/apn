import os
import pickle
import sqlite3

import jellyfish

PWD = os.path.abspath(os.path.dirname(__file__))


def dict_factory(cursor, row):
    return dict((col[0], row[idx]) for idx, col in enumerate(cursor.description))


def pickle_data():
    dbpath = os.path.abspath(os.path.join(PWD, 'apn.db'))
    conn = sqlite3.connect(dbpath)
    conn.row_factory = dict_factory

    c = conn.cursor()
    c.execute("""SELECT * FROM apn ORDER BY id""")

    apns_to_add = []
    for row in c:
        row['county_name_metaphone'] = jellyfish.metaphone(row['county'])
        row['state_name_metaphone'] = jellyfish.metaphone(row['state'])
        apns_to_add.append(row)

    pkl_path = os.path.abspath(os.path.join(PWD, 'apn', 'apns.pkl'))

    with open(pkl_path, 'wb') as pkl_file:
        pickle.dump(apns_to_add, pkl_file)


def build():
    pickle_data()


if __name__ == '__main__':
    build()
