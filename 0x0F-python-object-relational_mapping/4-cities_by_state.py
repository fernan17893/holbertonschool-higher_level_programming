#!/usr/bin/python3
"""
list all cities from database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb
db = MySQLdb.connect(host="localhost", port=3306, user="root",
                     passwd=argv[2], db=argv[3])

cur = db.cursor()
cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id")
for row in cur.fetchall():
    print(row)
cur.close()
db.close()
