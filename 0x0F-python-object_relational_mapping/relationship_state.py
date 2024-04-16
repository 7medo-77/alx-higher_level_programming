#!/usr/bin/python3
"""
Python module which defines a
class State and connects class to database
"""


from relationship_city import City
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states')

    def __repr__(self):
        rep = "{}: {}".format(self.id, self.name)
        return (rep)
