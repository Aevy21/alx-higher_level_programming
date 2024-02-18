#!/usr/bin/python3
"""
This script retrieves and displays all cities from the database specified.
It takes three arguments: MySQL username, MySQL password, and database name.
"""

import MySQLdb
from sys import argv


def list_all_cities(username, password, database_name):
    """
    Retrieve and display all cities from the specified database.

    :param username: MySQL username
    :param password: MySQL password
    :param database_name: Name of the database
    """
    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database_name)
        cur = db.cursor()

        # Execute the query to select all cities
        cur.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
        """)

        # Fetch and display results
        all_cities = cur.fetchall()
        for city in all_cities:
            print(city)

    except MySQLdb.Error as e:
        print(f"Error accessing MySQL: {e}")

    finally:
        # Close cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: script.py <username> <password> <database_name>")
        exit(1)

    list_all_cities(argv[1], argv[2], argv[3])
