#!/usr/bin/python3
"""
Connects to a MySQL database and retrieves all states from the table.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    
    cur = conn.cursor()

    # Use a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cur.execute(query, (sys.argv[4],))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
