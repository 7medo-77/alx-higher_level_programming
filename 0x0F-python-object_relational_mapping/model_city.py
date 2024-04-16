#!/usr/bin/python3
"""
Python module which defines a
class State and connects class to database
"""


from sqlalchemy import String, Integer, Column, ForeignKey
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """State class"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    # state = relationship("State", backref='states')

    def __repr__(self):
        rep = "{}: ({}) {}".format(self.state_id, self.id, self.name)
        return (rep)
