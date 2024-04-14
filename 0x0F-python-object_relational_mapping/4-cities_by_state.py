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
    query = """
        SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON states.id = cities.state_id
        ORDER BY cities.id ASC
    """
    cur.execute(query)

    res_words = cur.fetchall()
    for word in res_words:
        print(word)

    cur.close()
    conn.close()
