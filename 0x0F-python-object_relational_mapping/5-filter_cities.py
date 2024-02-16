#!/usr/bin/python3
"""
This script takes the name of a state as an argument and lists all cities of that state
from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

def list_cities_by_state(username, password, database_name, state_name):
    """
    Retrieve and display all cities of the specified state from the database.

    :param username: MySQL username
    :param password: MySQL password
    :param database_name: Name of the database
    :param state_name: Name of the state
    """
    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database_name)
        cur = db.cursor()

        # Execute the parameterized query to select cities from the specified state
        cur.execute("""
            SELECT * FROM cities
            WHERE state_name = %s
            ORDER BY cities.id ASC
        """, (state_name,))

        # Fetch and display results
        cities = cur.fetchall()
        if cities:
            for city in cities:
                print(city[0])
        else:
            print("No cities found for the specified state.")

    except MySQLdb.Error as e:
        print(f"Error accessing MySQL: {e}")

    finally:
        # Close cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, database_name, state_name)

