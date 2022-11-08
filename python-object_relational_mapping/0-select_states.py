#!/usr/bin/python3

""" script that lists all states from the database hbtn_0e_0_usa """


import MySQLdb
from sys import argv


if __name__ == '__main__':

    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               password=argv[2], database=argv[3])

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()

    for row in states:
        print(row)

    cursor.close()
    database.close()
