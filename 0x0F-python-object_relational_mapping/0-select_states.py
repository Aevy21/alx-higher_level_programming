#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all states from the 'states' table,
displaying them sorted in ascending order by their IDs.
"""

import sys
import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    charset="utf8"
)
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

