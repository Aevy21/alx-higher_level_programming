#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def print_state_by_name():
    """
    Retrieve and print the State object with the name passed as an argument
    from the specified database.
    """
    try:
        # Create engine and bind session
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query for the State object with the specified name
        state = session.query(State).filter(State.name == sys.argv[4]).first()

        
        if state:
            print(state.id)
        else:
            print("Not found")

    except Exception as e:
        print(f"Error accessing MySQL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(" ./script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    print_state_by_name()
