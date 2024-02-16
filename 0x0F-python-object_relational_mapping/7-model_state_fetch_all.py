#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def list_all_states():
    """
    Retrieve and display all State objects from the specified database.
    """
    try:
        # Create engine and bind session
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Fetch and display results
        all_states = session.query(State).order_by(State.id).all()
        if all_states:
            for state in all_states:
                print(f"{state.id}: {state.name}")
        else:
            print("No states found in the database.")

    except Exception as e:
        print(f"Error accessing MySQL: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database_name>")
        sys.exit(1)

    list_all_states()
