#!/usr/bin/python3
"""
This script changes the name of a State object from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def change_state_name():
    """
    Change the name of a State object with id=2 to "New Mexico" in the specified database.
    """
    try:
        # Create engine and bind session
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query for the State object with id=2 and change its name
        state_to_change = session.query(State).filter_by(id=2).first()
        if state_to_change:
            state_to_change.name = "New Mexico"
            session.commit()

    except Exception as e:
        print(f"Error accessing MySQL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database_name>")
        sys.exit(1)

    change_state_name()
