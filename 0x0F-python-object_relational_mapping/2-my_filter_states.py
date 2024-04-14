#!/usr/bin/python3
"""Python script which selects some states from table states"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            database=argv[3],
        )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE `name`= {} ".format(argv[4]))

    n_words = cur.fetchall()

    for word in n_words:
        print(word)
    cur.close()
    conn.close()
