# Damon Dix

import sqlite3

"""
Class for creating database, should only need to happen once, mostly for testing
purposes once initially create
"""


class MemberDB:

    def __init__(self):
        self.conn = sqlite3.connect("members.db")
        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS members (
            first_name text,
            last_name text,
            email text,
            phone_number text,
            address text )
         """)

        self.conn.commit()
        self.conn.close()

    """
    Function takes in literal values and inserts them into db, order of arguments
    is important
    """
    @staticmethod
    def add_member(fname, lname, email, address, number):
        conn = sqlite3.connect("members.db")
        cur = conn.cursor()
        member = [fname, lname, email, number, address]
        cur.executemany("""INSERT INTO members (first_name, last_name, email, phone_number, address)
        Values(?,?,?,?,?)""", [member],)

        conn.commit()
        conn.close()

