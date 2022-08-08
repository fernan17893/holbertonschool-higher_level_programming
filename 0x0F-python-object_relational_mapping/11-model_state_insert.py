#!/usr/bin/python3
"""
script prints  state object from database with the name passed as argument
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
    row = State(name="Lousiana")
    sess.add(row)
    sess.commit()
    print(row.id)
    sess.close()
