import sqlite3
from datetime import datetime, timedelta

"""
Class for creating database, should only need to happen once, mostly for testing
purposes once initially create
"""


class UserDB:
    def __int__(self):
        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS user (
                   id INTEGER PRIMARY KEY,
                   first_name text,
            last_name text,
            email text,
            phone_number text,
            address text,
            userName text,
            password text,
            age INTEGER
            )""")

        new_column = "ALTER TABLE USER ADD COLUMN Bookings CHAR(500)"

        self.cur.execute(new_column)

        self.conn.commit()
        self.conn.close()

    def create_table(self):

        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS user (
                           id INTEGER PRIMARY KEY,
                           first_name text,
                    last_name text,
                    email text,
                    phone_number text,
                    address text,
                    userName text,
                    password text,
                    age INTEGER
                    )""")

        conn.commit()

        conn.close()

    def add_User(self, fname, lname, email, address, number, userName, password, age):
        print(f'fName:{fname}, lName:{lname}, email:{email}, number:{number}, userName: {userName}, password: {password}, age: {age}')
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        client = [fname, lname, email, number, address, userName, password, age]
        cur.executemany("""INSERT INTO user (first_name, last_name, email, phone_number, address, userName, password, age)
        Values(?,?,?,?,?,?,?,?)""", [client], )

        conn.commit()
        conn.close()
