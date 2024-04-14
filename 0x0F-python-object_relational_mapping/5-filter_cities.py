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
    arg = argv[4].split()[0]

    query = """SELECT cities.name FROM cities
        JOIN states ON states.id = cities.state_id
        WHERE states.name = '{}'
        ORDER BY cities.id ASC""".format(arg)

    cur.execute(query)

    res_words = cur.fetchall()

    for index, word in enumerate(res_words):
        print("{}".format(word[0])) if index == len(res_words) - 1 else print("{},".format(word[0]), end="")

    cur.close()
    conn.close()
