#!/usr/bin/python3
"""
model_city Module.
this module contains City Model.
"""

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
        Class city.
        attributes:
            - id: integer, primary key, unique.
            - name: string 128 bits
            - state_id! integer, primary key, unique.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
