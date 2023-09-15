#!/usr/bin/python3
"""
    model_state Module.
    Class model of state used to store and fetch data from
    mysql database.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


Base = declarative_base()


class State(Base):
    """
        Class State
        to create states in MySQL databases.
    """
    __tablename = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
