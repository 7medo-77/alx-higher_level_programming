#!/usr/bin/python3
"""Python script which selects some states from table states"""


import MySQLdb
from sys import argv

conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
    )
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE states.name LIKE "N%"")

n_words = cur.fetchall()

for word in n_words:
    print(word)
cur.close()
conn.close()
