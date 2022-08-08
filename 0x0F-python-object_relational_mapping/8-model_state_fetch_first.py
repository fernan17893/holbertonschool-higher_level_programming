#!/usr/bin/python3
"""
script prints first state object from database
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
    query = sess.query(State).first()
    if query:
        print("{}: {}".format(query.id, query.name))
    else:
        print("Nothing")
    sess.close()
