#!/usr/bin/python3

import MySQLdb as sdb
import sys

if __name__ == "__main__":

    with sdb.connect(host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3]) as database:
        with database.cursor() as cursor:
            query = '''SELECT *
            FROM states
            WHERE BINARY name=%s
            '''
            search = sys.argv[4]
            cursor.execute(query, (search,))
            datas = cursor.fetchall()
            for data in datas:
                print(data)

