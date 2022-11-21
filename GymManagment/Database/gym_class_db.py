import sqlite3 as sq

class GymClass:

    def create_tables(self):
        # Connecting to sqlite
        connection_obj = sq.connect("Database.db")

        # cursor object
        cur = connection_obj.cursor()

        cur.execute("CREATE TABLE CLASSES (id TEXT, name TEXT, time")


        # Display table
        data = cur.execute("SELECT * FROM USER")
        print('USERS Table:')
        for row in data:
            print(row)

        connection_obj.commit()

        # Close the connection
        connection_obj.close()