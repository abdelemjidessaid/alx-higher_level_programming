#!/usr/bin/python3
"""
model_city_fetch_by_state Module.
Program that prints all cities from hbtn_0e_14_usa database.
Usage:
    ./14-model_city_fetch_by_state <mysql username>
                                    <mysql password>
                                    <database name>
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    cities = session.query(State, City).filter(State.id == City.state_id)
    for ci in cities:
        print("{}: ({}) {}".format(ci.State.name, ci.City.id, ci.City.name))

    session.close()
