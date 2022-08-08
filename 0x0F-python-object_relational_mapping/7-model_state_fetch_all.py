#!/usr/bin/python3
"""
script lists all State objects from hbtn_0e_6_usa
taking 3 arguments: mysql username, password, and db name
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                           argv[2], argv[3]))
    Session = sessionmaker()
    sess = Session(bind=engine)
    Base.metadata.create_all(engine)
    for state in sess.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    sess.close()
