#!/usr/bin/python3
"""select and filter using parameterization"""

import MySQLdb as sdb
import sys
if __name__ == "__main__":

    with sdb.connect(
            host="localhost", user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3]) as database:
        cursor = database.cursor()
        query = '''SELECT *
        FROM states
        WHERE name LIKE '{}'
        '''.format(sys.argv[4])
        cursor.execute(query)
        datas = cursor.fetchall()
        for data in datas:
            print(data)
