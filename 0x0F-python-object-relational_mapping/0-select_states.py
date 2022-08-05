#!/usr/bin/python3
"""
list all states from database
"""
from sys import argv
import MySQLdb
db = MySQLdb.connect(host="localhost", port=3306, user="root",
                     passwd=argv[2], db=argv[3])

cur = db.cursor()
cur.execute("select * FROM states order by id ASC")
for row in cur.fetchall():
    print(row)
cur.close()
db.close()
