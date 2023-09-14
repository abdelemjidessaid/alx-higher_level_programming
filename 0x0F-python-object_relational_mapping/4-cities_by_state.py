#!/usr/bin/python3

import sys
import MySQLdb


"""
    cities_by_state Module
    this program lists all cities from cities table in a database.
    args:
        1: mysql username
        2: mysql password
        3: database name
"""


def main():
    """
        function main is the entry point of program.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = conn.cursor()
    query = """
    SELECT c.id, c.name FROM state s, cities c 
    WHERE c.state_id = s.id 
    ORDER BY id ASC
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    for r in rows:
        print(r)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
