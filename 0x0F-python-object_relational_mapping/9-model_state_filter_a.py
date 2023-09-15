#!/usr/bin/python3
"""
model_state_filter Module
program that prints all state that starts with letter 'a'
in 'hbtn_0e_6_usa' database.
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(State)
    session = Session()

    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
