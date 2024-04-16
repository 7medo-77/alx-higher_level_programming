#!/usr/bin/python3
"""
Python module which defines a
class State and connects class to database
"""


from relationship_state import Base, State
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, Column, ForeignKey


class City(Base):
    """State class"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', backref='cities')

    def __repr__(self):
        rep = "{}: {}".format(self.id, self.name)
        return (rep)
