#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    res_obj = session.query(City, State)\
        .join(State, City.state_id == State.id)\
        .order_by(City.id)

    for obj in res_obj.all():
        print("{}: ({}) {}".format(obj.State.name, obj.City.id, obj.City.name))

    session.commit()
    session.close()
