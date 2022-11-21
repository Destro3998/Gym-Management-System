import sqlite3

class EquipmentDB:
    def create_tables(self):

        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()

        res=self.cur.execute("""CREATE TABLE IF NOT EXISTS equipments (
            id INTEGER PRIMARY KEY,
            title text,
            desc  text
            )""")

        self.conn.commit()

        self.conn.close()

    def add_equipments(self,title, desc):
        try:
            conn = sqlite3.connect("Database.db")
            cur = conn.cursor()
            d = [title, desc]
            res = cur.executemany("""INSERT INTO equipments (title, desc)
                        Values(?,?)""", [d], )

            conn.commit()
            conn.close()
            return True
        except Exception as ex:
            print(ex)
            return  False
    def get_equipments(self):
        try:
            conn = sqlite3.connect("Database.db")
            # conn.row_factory = self.dict_factory
            cur = conn.cursor()

            res = cur.execute("""select * from equipments""")
            res= res.fetchall()
            conn.commit()
            conn.close()
            dict={}

            for i in range(len(res),):
                dict[i]=res[i]
            return dict
        except Exception as ex:
            print(ex)
            return  False

    def dict_factory(self,cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d