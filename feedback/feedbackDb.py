import sqlite3 as sq

"""
class for feedback input 
"""

class Feedback:

    def __init__(self):
        self.conn = sq.connect("feedback.db")
        self.cur = self.conn.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS feedbacks (
                            full_name text,
                            email text,
                            phone_number text,
                            subject text,
                            feedback text,
                            experience text)""")

        self.conn.commit()
        self.conn.close()

    @staticmethod
    def add_user(fullname, email, phone_no, subject, feedback, experience):
        conn = sq.connect("feedback.db")
        cur = conn.cursor()
        user = [fullname, email, phone_no, subject, feedback, experience]
        cur.executemany("""INSERT INTO feedbacks (full_name, email, phone_number, subject, feedback, experience)
                Values(?,?,?,?,?, ?)""", [user], )

        conn.commit()
        conn.close()