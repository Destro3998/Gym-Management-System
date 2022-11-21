import sqlite3


class PlanDB:
    def create_tables(self):
        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS members (
            first_name text,
            last_name text,
            email text,
            phone_number text,
            address text,
            id text)
         """)

        self.conn.commit()
        self.conn.close()

        @staticmethod
        def create_plan(title, price, duration, status):
            conn = sqlite3.connect("Database.db")
            cur = conn.cursor()
            plan = [title, price, duration, status]
            cur.executemany("""INSERT INTO members (title, price, duration, status)
                Values(?,?,?,?)""", [plan], )

            conn.commit()
            conn.close()
