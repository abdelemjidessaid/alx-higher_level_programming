#!/usr/bin/python3
"""
my_filter_state Module
this program search for a keyword in a table from a database.
Usage:
    ./2-my_filter_states mysql_user mysql_passwd mysql_db state_name
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name)
    cursor = db.cursor()
    query = f"""
        SELECT * FROM state
        WHERE name LIKE BINARY '{state_name}'
        ORDER BY id ASC"""
    cursor.execute(query)

    rows = cursor.fetchall()

    for r in rows:
        print(r)

    cursor.close()
    db.close()
