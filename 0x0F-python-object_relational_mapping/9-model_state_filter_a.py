#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def list_states_with_letter_a():
    """
    Retrieve and display all State objects containing the letter 'a'
    from the specified database.
    """
    try:
        # Create engine and bind session
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and print State objects containing the letter 'a'
        states_with_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()
        if states_with_a:
            for state in states_with_a:
                print(f"{state.id}: {state.name}")
        else:
            print("Nothing")

    except Exception as e:
        print(f"Error accessing MySQL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database_name>")
        sys.exit(1)

    list_states_with_letter_a()
