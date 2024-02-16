#!/usr/bin/python3
"""
Retrieve and display values in the 'states' table
matching the provided state name, preventing SQL injection.

Parameters:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database
    - state_name: Name of the state to search for
"""

import MySQLdb
import sys


def search_states(username, password, database, state_name):
    """
    Connects to a MySQL database and retrieves states matching the provided name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.
        state_name (str): Name of the state to search for.
    """
    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Use a parameterized query to prevent SQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get the command-line arguments
    username, password, database, state_name = sys.argv[1:]

    # Call the function to search for states
    search_states(username, password, database, state_name)
