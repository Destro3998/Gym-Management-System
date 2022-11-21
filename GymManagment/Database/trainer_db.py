import sqlite3


class TrainerDB:
    def create_tables(self):
        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()

        res=self.cur.execute("""CREATE TABLE IF NOT EXISTS trainer (
            id INTEGER PRIMARY KEY,
            fName text,
            lName text,
            email text,
            phone text,
            address text,
            specialist text
            )
         """)

        self.conn.commit()

        self.conn.close()

    def get_all_trainers(self):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        res = cur.execute(f"SELECT fName, lName FROM trainer")
        res = res.fetchall()
        conn.commit()
        print(f'..................Trainer.......{res}')
        conn.close()
        return res

    def create_trainer(self, fName, lName, email, phone, address, specialist):
        try:
            conn = sqlite3.connect("Database.db")
            cur = conn.cursor()
            trainer = [fName, lName, email, phone, address, specialist]
            res = cur.executemany("""INSERT INTO trainer (fName, lName, email, phone, address, specialist)
                        Values(?,?,?,?,?,?)""", [trainer], )
            print(res.fetchone())
            conn.commit()
            conn.close()
            return True
        except:
            return  False
