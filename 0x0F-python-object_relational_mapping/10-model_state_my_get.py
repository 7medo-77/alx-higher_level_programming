#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    states = session.query(State)\
                    .filter(State.name == sys.argv[4])\
                    .order_by(State.id)
    if states:
        for state in states:
            print(state.id)
        print(states)
    else:
        print("Not found")
        print(states)

    session.commit()
    session.close()
