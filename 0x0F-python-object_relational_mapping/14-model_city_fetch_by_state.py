#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


def fetch_cities_by_state():
    """
    Fetch and print all City objects from the specified database.
    """
    try:
        # Create engine and bind session
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and print all City objects
        cities = session.query(City, State).join(State).order_by(City.id).all()
        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")

    except Exception as e:
        print(f"Error accessing MySQL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: ./python_file.py <username> <password> <database_name>")
        sys.exit(1)

    fetch_cities_by_state()
