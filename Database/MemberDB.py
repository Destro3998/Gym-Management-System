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

        #self.cur.execute("""CREATE TABLE members (
        #    first_name text,
        #    last_name text,
        #    email text,
        #    phone_number integer,
        #    address text )
        #""")


        # conn.commit()



