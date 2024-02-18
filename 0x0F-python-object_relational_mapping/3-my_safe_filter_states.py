#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa

where name matches the argument, safely from MySQL injections.
"""

import MySQLdb
from sys import argv

def display_states():
    """
    Connect to the database and display values from the states table
    where the name matches the argument, safely from MySQL injections.
    """
    try:
        # Connect to the database using command-line arguments
        db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()

        # Get the state name argument from command-line
        state_name = argv[4]

        # Execute the query with parameters to avoid MySQL injections
        cur.execute("""
            SELECT * FROM states
            WHERE name = %s
            ORDER BY id ASC
        """, (state_name,))

        # Fetch and display results
        states = cur.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error accessing MySQL: {e}")

    finally:
        # Close cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: ./script.py <username> <password> <database_name> <state_name>")
        exit(1)

    display_states()
