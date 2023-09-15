#!/usr/bin/python3
"""
model_state_my_get Module
Program that prints a state given as an argument.
Usage:
    ./10-model_state_my_get 1 2 3 4
    1: mysql username
    2: mysql password
    3: database name
    4: state name to search
"""


from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(State)
    Base.metadata.create_all(engine)
    session = Session()

    result = session.query(State).filter(
        State.name == argv[4]
    ).one_or_none()
    print(result)

    session.close()
