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
    # arg = argv[4].split()[0]
    query = """
        SELECT cities.name FROM cities
        JOIN states ON states.id = cities.state_id
        ORDER BY cities.name;
    """

    cur.execute(query)

    res_words = cur.fetchall()

    for index, word in enumerate(res_words):
        print("{}".format(word)) if index < len(res_words) else print("{},".format(word), end="")

    cur.close()
    conn.close()
