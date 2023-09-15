#!/usr/bin/python3
"""
cities_by_state Module
this program lists all cities from cities table in a database.
usage:
    ./4-cities_by_state 1 2 3
args:
    1: mysql username
    2: mysql password
    3: database name
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    cursor = conn.cursor()
    query = """
    SELECT `c`.`id`, `c`.`name`, `s`.`name`
    FROM `cities` as `c`
    INNER JOIN `states` as `s`
    ON `c`.`state_id` = `s`.`id`
    ORDER BY `c`.`id`
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    for r in rows:
        print(r)
