#!/usr/bin/python3

"""Script to create a State with the City in the database. """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """
    Script to create a State with the City in the database.

    Args:
        sys.argv[1] (str): MySQL username.
        sys.argv[2] (str): MySQL password.
        sys.argv[3] (str): Database name.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db_conn = f"mysql://{username}:{password}@localhost:3306/{database_name}"
    # Create engine
    engine = create_engine(db_conn)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California" with the City "San Francisco"
    california = State(name="California", cities=[City(name="San Francisco")])
    
    session.add(california)
    session.commit()
