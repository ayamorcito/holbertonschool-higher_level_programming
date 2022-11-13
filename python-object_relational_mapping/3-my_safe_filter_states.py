#!/usr/bin/python3
""" Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, 
safe from MySQL injections """


import MySQLdb
from sys import argv

if __name__ == '__main__':

    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s\
                ORDER BY states.id ASC", (argv[4],))
    states = cursor.fetchall()

    for row in states:
        print(row)

    cursor.close()
    database.close()
