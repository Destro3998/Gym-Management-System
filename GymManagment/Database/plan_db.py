import sqlite3


class PlanDB:
    def create_tables(self):
        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()

        res=self.cur.execute("""CREATE TABLE IF NOT EXISTS plans (
            id INTEGER PRIMARY KEY,
            title text,
            price INTEGER,
            email text,
            duration text,
            status text
            )
         """)

        self.conn.commit()

        self.conn.close()

    def create_plan(self,title, price, duration, status):
        try:
            conn = sqlite3.connect("Database.db")
            cur = conn.cursor()
            plan = [title, price, duration, status]
            res = cur.executemany("""INSERT INTO plans (title, price, duration, status)
                        Values(?,?,?,?)""", [plan], )
            print(res.fetchone())
            conn.commit()
            conn.close()
            return True
        except:
            return  False
