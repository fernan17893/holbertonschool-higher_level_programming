#!/usr/bin/python3
"""
script prints all state objects from database containing the letter 'a'
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
    query = sess.query(State).filter(State.name.like('%a%'))\
                             .order_by(State.id)
    for _row in query.all():
        print("{}: {}".format(_row.id, _row.name))
    sess.close()
