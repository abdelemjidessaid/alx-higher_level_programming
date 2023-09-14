#!/usr/bin/python3

from MySQLdb import _mysql
import sys

"""
    select_state Module.
"""


def main():
    """
        main function which is the entry point of program.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = _mysql.connect(host="localhost", user=username,
                        password=password, database=db_name, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for r in rows:
        print(r)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
