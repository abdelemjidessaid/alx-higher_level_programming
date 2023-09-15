#!/usr/bin/python3

"""
    filter_state Module
    this program fetch all state names from state table,
    and display it.
    Usage:
        Usage: ./1-filter_states.py <mysql username> \
                             <mysql password> \
                             <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM `state` WHERE `name` LIKE 'N%' ORDER BY `id` ASC"
    )

    rows = cursor.fetchall()

    for r in rows:
        print(r)

    cursor.close()
    db.close()
