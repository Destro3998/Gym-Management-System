import sqlite3


class BookingDB:
    def create_tables(self):
        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()

        res=self.cur.execute("""CREATE TABLE IF NOT EXISTS booking (
            id INTEGER PRIMARY KEY,
            title text,
            duration INTEGER
            )
         """)

        self.conn.commit()

        self.conn.close()

    def add_booking(self,title, duration):
        try:
            conn = sqlite3.connect("Database.db")
            cur = conn.cursor()
            booking = [title, duration]
            res = cur.executemany("""INSERT INTO booking (title, duration)
                        Values(?,?)""", [booking], )
            print(res.fetchone())
            conn.commit()
            conn.close()
            return True
        except:
            return  False
