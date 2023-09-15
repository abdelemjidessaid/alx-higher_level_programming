#!/usr/bin/python3
"""
model_state_insert Module
Program that adds the State object “Louisiana” to the database hbtn_0e_6_usa
Usage:
    ./11-model_state_insert <mysql username> <mysql password> <database name>
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    state_add = session.query(State).filter(State.name == 'Louisiana').one()
    print(state_add.id)

    session.close()
