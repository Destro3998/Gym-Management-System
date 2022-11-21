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


class MemberPlanDB:
    """
    Function takes in literal values and inserts them into db, order of arguments
    is important
    """

    def create_tables(self):
        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()
        res = self.cur.execute("""CREATE TABLE IF NOT EXISTS members_plans (
                          id INTEGER PRIMARY KEY,
                          member_id text,
                   plan_id text,
                   price INTEGER,
                   start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  end_date TIMESTAMP
                          )
                       """)

    def create_memeber_plan(self, m_id, p_id, p, d):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        data = [m_id, p_id, p, str(datetime.now() + timedelta(days=d * 30))]
        res = cur.execute(f'insert into members_plans(member_id,plan_id,price,end_date) values(?,?,?,?)', (data,))

        conn.commit()
        conn.close()
        return res
