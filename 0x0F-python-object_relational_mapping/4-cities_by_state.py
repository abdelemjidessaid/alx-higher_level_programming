#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
Usage: ./4-cities_by_state.py <mysql username> \
                              <mysql password> \
                              <database name>
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf-8"
    )

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
