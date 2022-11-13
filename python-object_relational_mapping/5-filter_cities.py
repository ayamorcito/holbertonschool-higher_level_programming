#!/usr/bin/python3
""" A script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_use """


import MySQLdb
from sys import argv

if __name__ == '__main__':

    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               password=argv[2], database=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT cities.name FROM cities, states\
                WHERE cities.state_id = states.id AND states.name=%s\
                ORDER BY cities.id", (argv[4],))
    table = cursor.fetchall()

try:
    for row in range(len(table) - 1):
        print(table[row][0], end=', ')
    print(table[row + 1][0])
except Exception:
    print()

cursor.close()
database.close()
