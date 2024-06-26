#!/usr/bin/python3
"""using select statement to query database"""

import MySQLdb as sdb
import sys
if __name__ == "__main__":

    with sdb.connect(
            host="localhost", user=sys.argv[1], password=sys.argv[2],
            database=sys.argv[3]) as database:
        with database.cursor() as cursor:
            query = '''SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON  states.id = cities.state_id
            WHERE BINARY states.name = %s
            ORDER BY cities.id ASC;
            '''
            search = sys.argv[4]
            cursor.execute(query, (search,))
            datas = cursor.fetchall()
            for data in datas:
                print(data)
