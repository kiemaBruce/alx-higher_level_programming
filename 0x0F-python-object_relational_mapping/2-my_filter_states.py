#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mySQL_username = sys.argv[1]
    mySQL_password = sys.argv[2]
    mySQL_database = sys.argv[3]
    state_name = sys.argv[4]
    conn = None
    try:
        conn = MySQLdb.connect(host="localhost", user=mySQL_username,
                               passwd=mySQL_password, db=mySQL_database,
                               port=3306)
        cur = conn.cursor()
        query = "SELECT * FROM states WHERE name LIKE %s order by id ASC"
        """for matching the substring within a larger string"""
        """cur.execute(query, (f"%{state_name}%",))"""
        cur.execute(query, (state_name,))
        states = cur.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
