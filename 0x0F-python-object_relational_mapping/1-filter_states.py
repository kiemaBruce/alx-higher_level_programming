#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = None
    try:
        mySQL_username = sys.argv[1]
        mySQL_password = sys.argv[2]
        mySQL_database = sys.argv[3]
        conn = MySQLdb.connect(host="localhost", user=mySQL_username,
                               passwd=mySQL_password, db=mySQL_database,
                               port=3306)
        cur = conn.cursor()
        query = "SELECT * FROM states WHERE name LIKE 'N%' order by id ASC"
        cur.execute(query)
        states = cur.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
