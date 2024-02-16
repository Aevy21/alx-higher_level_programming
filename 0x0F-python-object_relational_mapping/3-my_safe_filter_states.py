#!/usr/bin/python3
"""
Filter and display values in the 'states' table
matching the provided state name.

Parameters:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database
    - state_name: Name of the state to filter and display
"""
from sys import argv
import MySQLdb
import sys


def filter_states(username, password, db_name, state_name):
    """
    Connects to a MySQL database and retrieves states matching the provided name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Name of the database.
        state_name (str): Name of the state to filter and display.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Use a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s"
    cursor.execute(query, (state_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(argv[0]))
        sys.exit(1)

    # Call the function to filter states
    filter_states(argv[1], argv[2], argv[3], argv[4])
