#!/usr/bin/python3
import MySQLdb 
import sys

conn = MySQLdb.connect(
            host= "localhost",
            port = 3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
        )
cur = conn.cursor()
conn.execute("SELECT * FROM states ORDER BY `id` ASC")

results = conn.fetchall()
for row in results:
    print(row)
