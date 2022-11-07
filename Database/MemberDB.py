# Damon Dix

import sqlite3


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



