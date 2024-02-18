#!/usr/bin/python3
"""
Connects to a MySQL database and retrieves all states with names starting with 'N'.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()

    # Execute the query to retrieve states starting with 'N' (case-sensitive)
    cur.execute("SELECT id, name FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch and display results
    query_rows = cur.fetchall()
    if query_rows:
        for row in query_rows:
            print(row)  # Print the state ID and state name
    else:
        print("No states found with names starting with 'N'")

    # Close cursor and database connection
    cur.close()
    conn.close()
