#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usas """


import MySQLdb
from sys import argv

if __name__ == '__main__':

    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               password=argv[2], database=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM states\
                JOIN cities ON states.id = cities.state_id\
                ORDER BY cities.id")
    table = cursor.fetchall()

    for row in table:
        print(row)

    cursor.close()
    database.close()
