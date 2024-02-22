#!/usr/bin/python3
"""
Script to list all State objects and corresponding City objects in the database hbtn_0e_101_usa.

Usage:
    python script.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def main():
    """
    Main function to list all State objects and corresponding City objects.
    """
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db_connection_string = f"mysql://{username}:{password}@localhost:3306/{database_name}"

    engine = create_engine(db_connection_string)
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_cities = (
        session.query(State)
        .outerjoin(City)
        .order_by(State.id, City.id)
        .all()
    )

    for state in states_with_cities:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

if __name__ == "__main__":
    main()
