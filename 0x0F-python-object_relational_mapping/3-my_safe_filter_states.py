#!/usr/bin/python3

import sys
import MySQLdb


"""
    my_safe_filter_states Module
    this program search for a keyword in a table from a database.
"""


def main():
    """
        main function is the entry point of program.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    query = "SELECT * FROM state WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name, ))

    rows = cursor.fetchall()

    for r in rows:
        print(r)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
