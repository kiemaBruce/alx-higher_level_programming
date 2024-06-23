#!/usr/bin/python3
"""Lists all cities in a certain state from hbtn_0e_0_usa database
and protects from SQL injection"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mySQL_username = sys.argv[1]
    mySQL_password = sys.argv[2]
    mySQL_database = sys.argv[3]
    state = sys.argv[4]
    conn = None
    try:
        conn = MySQLdb.connect(host="localhost", user=mySQL_username,
                               passwd=mySQL_password, db=mySQL_database,
                               port=3306)
        cur = conn.cursor()
        query = """SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states
        ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC"""
        cur.execute(query, (state,))
        cities = cur.fetchall()
        for city in cities:
            print(city)
    except MySQLdb.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
