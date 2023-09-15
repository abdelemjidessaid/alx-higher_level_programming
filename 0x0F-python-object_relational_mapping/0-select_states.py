#!/usr/bin/python3

import MySQLdb
import sys

"""
    select_state Module.
"""


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    rows = cursor.fetchall()
    for r in rows:
        print(r)

    cursor.close()
    db.close()
