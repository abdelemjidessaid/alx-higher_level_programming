#!/usr/bin/python3

import sys
import MySQLdb


"""
    filter_state Module
    this program fetch all state names from state table,
    and display it.
"""


def main():
    """
        main function the entry point of program.
    """
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM state WHERE name LIKE 'N%' ORDER id ASC"
    )

    rows = cursor.fetchall()

    for r in rows:
        print(r)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
