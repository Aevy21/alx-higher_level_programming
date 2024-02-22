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
    username = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    db_connection_string = "mysql://{username}:{pwd}@localhost:3306/{db_name}"
    db_connection_string = db_connection_string.format(
        username=username, pwd=pwd, db_name=db_name)

    engine = create_engine(db_connection_string)
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
