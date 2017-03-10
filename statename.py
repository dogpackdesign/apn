import sqlite3, json



def main():
    file = open("states.json", "r")
    states = json.load(file)
    conn = sqlite3.connect('apn.db')
    sql = "update apn set state = ? where state_abbrev = ?"
    cur = conn.cursor()

    for abbr, name in states.iteritems():
        cur.execute(sql, (name, abbr))
    conn.commit()


if __name__ == '__main__':
    main()