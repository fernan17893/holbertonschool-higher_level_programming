#!/usr/bin/python3
"""
changes the name of a State object from database
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
    row = sess.query(State).filter_by(id='2').first()
    row.name = "New Mexico"
    sess.commit()
    sess.close()
