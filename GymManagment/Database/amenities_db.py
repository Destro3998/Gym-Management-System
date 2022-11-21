import sqlite3


class AmenitiesDB:
    def create_tables(self):
        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()

        res=self.cur.execute("""CREATE TABLE IF NOT EXISTS amenities (
            id INTEGER PRIMARY KEY,
            amenitiesString text
            )
         """)

        self.conn.commit()

        self.conn.close()

    def add_amenities(self, amenitiesString):
        try:
            conn = sqlite3.connect("Database.db")
            cur = conn.cursor()
            amenities = [amenitiesString]
            res = cur.executemany("""INSERT INTO amenities (amenitiesString)
                        Values(?)""", [amenities], )
            print(res.fetchone())
            conn.commit()
            conn.close()
            return True
        except:
            return  False
