import sqlite3

class timeSlotDB:

    def create_tables(self):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        res = cur.execute("""CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY,
            title text,
            start_time  text,
            end_time text
            )
         """)


        conn.commit()
        conn.close()

    def create_time_slots(self, title, froma, to, day):
        try:
            conn = sqlite3.connect("Database.db")
            cur = conn.cursor()
            plan = [title, froma, to, day]
            res = cur.executemany("""INSERT INTO classes (title, start_time, end_time, day)
                        Values(?,?,?,?)""", [plan], )
            #print(res.fetchone())
            conn.commit()
            conn.close()
            return True
        except Exception as ex:
            print(ex)
            return False

    def update_time(self, froma, to):
        try:
            conn = sqlite3.connect("Database.db")
            cur = conn.cursor()
            plan = [froma, to]
            res = cur.executemany("""INSERT INTO classes (start_time, end_time)
                              Values(?,?)""", [plan], )
            #print(res.fetchone())
            conn.commit()
            conn.close()
            return True
        except Exception as ex:
            print(ex)
            return False


    def get_time_slots(self):
        try:
            conn = sqlite3.connect("Database.db")
            conn.row_factory = self.dict_factory
            cur = conn.cursor()
            res = cur.execute("""SELECT * FROM classes""")
            data_1 = cur.fetchall()
            conn.commit()
            conn.close()
            dict={}
            for i,d in enumerate(data_1):
                dict[i] = d
            return dict
        except Exception as ex:
            print(ex)
            return []

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def delete_class(self, class_id):

        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        cur.execute("""DELETE FROM CLASSES WHERE id=?""", (class_id,))

        conn.commit()
        conn.close()

