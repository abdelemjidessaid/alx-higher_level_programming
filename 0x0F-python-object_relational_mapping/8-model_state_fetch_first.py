#!/usr/bin/python3
"""
model_state_fetch_first Module
this program prints the first state name from database hbtn_0e_6_usa
usage: ./8-model_state_fetch_first <mysql username> <mysql password>
                                    <database name>
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

    print(session.query(State).order_by(State.id)[0])
