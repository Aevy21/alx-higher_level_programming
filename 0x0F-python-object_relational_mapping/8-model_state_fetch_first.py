#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def print_first_state():
    """
    Retrieve and print the first State object from the specified database.
    """
    try:
        # Create engine and bind session
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and print the first State object
        first_state = session.query(State).order_by(State.id).first()
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")

    except Exception as e:
        print(f"Error accessing MySQL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database_name>")
        sys.exit(1)

    print_first_state()
