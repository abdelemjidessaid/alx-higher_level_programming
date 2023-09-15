#!/usr/bin/python3
"""
my_safe_filter_states Module
this program search for a keyword in a table from a database.
Usage: ./3-my_safe_filter_states <mysql username>\
                                <mysql password>\
                                <database name>\
                                <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf-8")
    cursor = db.cursor()
    query = "SELECT * FROM state WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4], ))

    rows = cursor.fetchall()

    for r in rows:
        print(r)

    cursor.close()
    db.close()
