#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def delete_states_with_letter_a():
    """
    Delete all State objects with a name containing the letter 'a'
    from the specified database.
    """
    try:
        # Create engine and bind session
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query for State objects with a name containing the letter 'a' and delete them
        states_to_delete = session.query(
            State).filter(State.name.like('%a%')).all()
        if states_to_delete:
            for state in states_to_delete:
                session.delete(state)
            session.commit()

    except Exception as e:
        print(f"Error accessing MySQL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database_name>")
        sys.exit(1)

    delete_states_with_letter_a()
