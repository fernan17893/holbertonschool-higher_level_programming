#!/usr/bin/python3
"""
list all states from database
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states\
    WHERE name = %s\
    ORDER BY id", (argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
