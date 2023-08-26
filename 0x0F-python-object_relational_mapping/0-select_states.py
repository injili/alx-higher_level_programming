#!/usr/bin/python3

import MySQLdb
from sys import argv

if len(sys.argv) = 4:
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    try:
        db = connect(host='localhost',
                     port='3306',
                     user=username,
                     passwd=password,
                     db=database)

        cursor = db.cursor()

        query = "SELECT * FROM states"
        cursor.execute(query)

        result = cursor.fetchall()
        for row in result:
            print(row)

        cursor.close()
        db.close()
