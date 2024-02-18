#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

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

        # Execute the query to select all cities of the specified state
        cur.execute("""
            SELECT name
            FROM cities
            WHERE state_id = (
                SELECT id
                FROM states
                WHERE name = %s
            )
            ORDER BY id ASC
        """, (state_name,))

        # Fetch and display results
        cities = cur.fetchall()
        if cities:
            city_names = ', '.join(city[0] for city in cities)
            print(city_names)

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

    list_cities_by_state(argv[1], argv[2], argv[3], argv[4])
