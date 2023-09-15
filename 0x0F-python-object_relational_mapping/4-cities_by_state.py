#!/usr/bin/python3
"""
cities_by_state Module
this program lists all cities from cities table in a database.
args:
    1: mysql username
    2: mysql password
    3: database name
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
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
