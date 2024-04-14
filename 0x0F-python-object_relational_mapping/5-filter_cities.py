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
    query = """
        SELECT cities.name FROM cities WHERE states.name = {}
        JOIN states ON states.id = cities.state_id
        GROUP BY states.name
        SORT BY cities.name
    """.format(arg)

    cur.execute(query)

    res_words = cur.fetchall()

    for index, word in enumerate(res_words):
        print("{}".format(word), end="") if not res_words[index + 1] else print("{},".format(word), end="")

    cur.close()
    conn.close()
