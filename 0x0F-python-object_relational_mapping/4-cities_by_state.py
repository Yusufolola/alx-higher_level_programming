#!/usr/bin/python3
"""using inner join statements to search in database"""

import MySQLdb as sdb
import sys
if __name__ == "__main__":

    with sdb.connect(
            host="localhost", user=sys.argv[1],
            password=sys.argv[2], database=sys.argv[3]) as database:
        with database.cursor() as cursor:
            query = '''SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON  states.id = cities.state_id
            ORDER BY cities.id ASC;
            '''
            cursor.execute(query)
            datas = cursor.fetchall()
            for data in datas:
                print(data)
