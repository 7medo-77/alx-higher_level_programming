#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                password=sys.argv[2],
                database=sys.argv[3],
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    conn.close()
