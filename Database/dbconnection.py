import sqlite3 as sq
from sqlite3 import Error


def connection():

    db_connect = None
    try:
        db_connect = sq.connect('database.db')
    except Error as e:
        print(e)

    return db_connect


if __name__ == "__main__":
    conn = connection()
    cur = conn.cursor()

    # user (firstname, lastname, email age, phone_number
    #        username, join_date, end_of membership, member_id)
    # cur.execute("""CREATE TABLE user (first_name text,\
    #                last_name text,\
    #                email text,\
    #                age integer, \
    #                address text, \
    #                phone_number integer,\
    #                memberID integer, username text)""")
    #
    # add_users = [
    #             ('Elle', 'James', 'jamesee@yahoo.com', 19, '221 Summer Blvd', 306873324, 11200, 'jam322'),
    #             ('Emily', 'geller', 'gelleremm@gmail.com', 30, '310 Fall Ave', 3061432134, 11100, 'gee000')
    # ]
    # cur.executemany("""INSERT INTO user VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", add_users)

    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.commit()
    conn.close()