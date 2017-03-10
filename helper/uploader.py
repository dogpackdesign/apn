import json

import sqlite3
import build


def main():
    # file = open('regex.json', 'r')
    # conn = sqlite3.connect('apn.db')
    # sql = '''INSERT INTO APN(apn_format, apn_regex, county, state, state_abbrev) VALUES(?, ?, ?, ?, ?)'''
    # cur = conn.cursor()
    # dict = json.load(file)
    # for state, value in dict.iteritems():
    #     for county, other2 in value.iteritems():
    #         for regex, format in zip(other2['regex'], other2['formats']):
    #             cur.execute(sql, (format, regex, county, None, state))
    # conn.commit()
    build.build()
    print 'hello'

if __name__ == '__main__':
    main()
