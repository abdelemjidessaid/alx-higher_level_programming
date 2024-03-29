#!/usr/bin/python3
"""
model_state_fetch_all Module
this program fetches all states from hbtn_0e_6_usa database.
usage:
    ./7-model_state_fetch_all <mysql user>
                                <mysql password>
                                <mysql database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
