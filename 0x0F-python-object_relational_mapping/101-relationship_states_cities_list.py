#!/usr/bin/python3
""" scipt to list all State objects corresponding to city """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """
    Script to list all State objects and corresponding City in the database.

    Args:
        sys.argv[1] (str): MySQL username.
        sys.argv[2] (str): MySQL password.
        sys.argv[3] (str): Database name.
    """
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Define database connection string
    db_connect = "mysql://{username}:{pwd}@localhost:3306/{db_name}"
    db_connect = db_connect.format(username=username, pwd=pwd, db_name=db_name)

    # Create engine
    engine = create_engine(db_connect)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all State objects and corresponding City objects
    states_with_cities = session.query(State).order_by(State.id).all()

    # Display results
    for state in states_with_cities:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
