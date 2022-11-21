import sqlite3
from datetime import datetime, timedelta

"""
Class for creating database, should only need to happen once, mostly for testing
purposes once initially create
"""


def get_memeber_plans(id):
    conn = sqlite3.connect("Database.db")
    cur = conn.cursor()

    res = cur.executemany(f"select * from members_plans as mp,plans as p where member_id={id} and plan_id=p.id")
    res = res.fetchall()
    conn.commit()
    conn.close()
    return res


class MemberDB:
    """
    Function takes in literal values and inserts them into db, order of arguments
    is important
    """

    def __int__(self):
        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()

        res = self.cur.execute("""CREATE TABLE IF NOT EXISTS members (
                   id INTEGER PRIMARY KEY,
                   first_name text,
            last_name text,
            email text,
            phone_number text,
            address text
                   )
                """)
        self.conn.commit()

        self.conn.close()

    def create_tables(self):
        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()

        res = self.cur.execute("""CREATE TABLE IF NOT EXISTS members (
                           id INTEGER PRIMARY KEY,
                           first_name text,
                    last_name text,
                    email text,
                    phone_number text,
                    address text
                           )
                        """)

        res = self.cur.execute("""CREATE TABLE IF NOT EXISTS members_plans (
                          id INTEGER PRIMARY KEY,
                          member_id text,
                   plan_id text,
                   price INTEGER,
                   start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  end_date TIMESTAMP
                          )
                       """)

        self.conn.commit()

        self.conn.close()

    def add_member(self, fname, lname, email, address, number):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        member = [fname, lname, email, number, address]
        cur.executemany("""INSERT INTO members (first_name, last_name, email, phone_number, address)
        Values(?,?,?,?,?)""", [member], )

        conn.commit()
        conn.close()

    def get_member_by_id(self, id):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        res = cur.execute(f"select * from members where id ={id}")
        res = res.fetchone()
        conn.commit()
        conn.close()
        return res

    def get_plans_by_id(self, id):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        res = cur.execute(f"select * from plans where id ={id}")
        res = res.fetchone()
        conn.commit()
        conn.close()
        return res

    def get_all_plans(self):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        res = cur.execute(f"SELECT * FROM plans")
        res = res.fetchall()
        conn.commit()
        conn.close()
        return res

    def create_memeber_plan(self, m_id, p_id, p, d):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        data = [m_id, p_id, p, datetime.now() + timedelta(days=d * 30)]
        res = cur.executemany(f"insert into members_plans(  member_id text,plan_id,price,end_date) value(?,?,?,?)",
                              [data])

        conn.commit()
        conn.close()
        return res
