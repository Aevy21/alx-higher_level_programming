#!/usr/bin/python3
"""
Script to list all City objects from the database hbtn_0e_101_usa.

Usage:
    python script.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """
Script to list all City objects from the database hbtn_0e_101_usa.

Usage:
    python script.py <username> <password> <database>
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db_url = "mysql://{username}:{password}@localhost:3306/{database_name}"
    db_url = db_url.format(username=username, password=password, db_name=db_name)

    db_engine = create_engine(db_url)
    Base.metadata.bind = db_engine

    Session = sessionmaker(bind=db_engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
