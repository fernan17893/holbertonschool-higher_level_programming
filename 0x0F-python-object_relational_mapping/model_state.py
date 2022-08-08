#!/usr/bin/python3
"""
file contains class definition of State
and instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class inherits from Base
    Attributes:
        id represents a column of unique integers, that cannont be null
        and is primary key, name reperesents string column with 128 characters
        max and cannot be null
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
