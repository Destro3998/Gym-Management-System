import sqlite3


class FeedbackDB:
    def create_tables(self):
        self.conn = sqlite3.connect("Database.db")
        self.cur = self.conn.cursor()

        res = self.cur.execute("""CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY,
            title text,
            feedback text
            
            )
         """)

        self.conn.commit()

        self.conn.close()

    def add_feedback(self, feedbackString, title):
        print(f'.................In DB............{title}')
        print(f'.................In DB............{feedbackString}')
        try:
            conn = sqlite3.connect("Database.db")
            cur = conn.cursor()
            feedback = [feedbackString, title]
            res = cur.executemany("""INSERT INTO feedback (title, feedback)
                        Values(?,?)""", [feedback],)
            print(f"............Success......{res.fetchone()}")
            conn.commit()
            conn.close()
            return True
        except:
            return False
