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
    """Represents a state for a MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
