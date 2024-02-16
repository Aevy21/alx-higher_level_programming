#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
"""

import MySQLdb
import sys

def list_all_states():
    """
    Retrieve and display all State objects from the specified database.
    """
    try:
        # Connect to the database using command-line arguments
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()

        # Execute the query to select all State objects
        cur.execute("SELECT id, name FROM states ORDER BY id ASC")

        # Fetch and display results
        all_states = cur.fetchall()
        if all_states:
            for state in all_states:
                print(f"{state[0]}: {state[1]}")  # Print only the state name
        else:
            print("No states found in the database.")

    except MySQLdb.Error as e:
        print(f"Error accessing MySQL: {e}")

    finally:
        # Close cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database_name>")
        sys.exit(1)

    list_all_states()

