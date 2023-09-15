#!/usr/bin/python3
"""
    filter_cities Module.
    this program lists cities of a given state.

    usage: ./5-filter_cities 1 2 3 4
    args:
        1: mysql username
        2: mysql password
        3: database name
        4: state name
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    state_name = argv[4]
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    cursor = conn.cursor()
    query = """SELECT cities.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC"""
    cursor.execute(query, (state_name, ))

    rows = cursor.fetchall()
    print(", ".join([city[0] for city in rows]))

    cursor.close()
    conn.close()
