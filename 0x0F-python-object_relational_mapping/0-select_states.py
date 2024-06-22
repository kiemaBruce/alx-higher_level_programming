#!/usr/bin/env python3
"""Lists all states from hbtn_0e_0_usa database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mySQL_username = sys.argv[1]
    mySQL_password = sys.argv[2]
    mySQL_database = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", user=mySQL_username,
                           passwd=mySQL_password, db=mySQL_database, port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states order by id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
