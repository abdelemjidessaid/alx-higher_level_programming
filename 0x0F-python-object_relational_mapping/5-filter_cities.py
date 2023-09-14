#!/usr/bin/python3

import sys
import MySQLdb


"""
    filter_cities Module.
    this program lists cities of a given state.

    args:
        1: mysql username
        2: mysql password
        3: database name
        4: state name
"""


def main():
    """
        main function is the entry point of program.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        db=db_name,
        user=username,
        passwd=password
    )

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


if __name__ == "__main__":
    main()
