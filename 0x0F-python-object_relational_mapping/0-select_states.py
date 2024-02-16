#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa: """
from sys import argv
import MySQLdb

if __name__ == "__main__":
    usr = argv[1]
    pw = argv[2]
    db_name = argv[3]
    host = "localhost"
    port = 3306

    db = MySQLdb.connect(host=host, port=port, user=usr, passwd=pw, db=db_name)
    interact_db = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    interact_db.execute(query)
    [print(states) for states in interact_db.fetchall()]

    db.close()
