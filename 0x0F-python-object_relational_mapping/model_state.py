#!/usr/bin/python3


"""
    model_state Module.
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
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
