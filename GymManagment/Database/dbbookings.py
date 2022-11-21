import sqlite3 as sq
from sqlite3 import Error

class MemberDB:

    def create_tables(self):
        # Connecting to sqlite
        connection_obj = sq.connect("Database.db")

        # cursor object
        cursor_obj = connection_obj.cursor()


        # Add a new column to geek table
        new_column = "ALTER TABLE USER ADD COLUMN Bookings CHAR(500)"

        cursor_obj.execute(new_column)

        # Display table
        data = cursor_obj.execute("SELECT * FROM USER")
        print('USERS Table:')
        for row in data:
            print(row)

        connection_obj.commit()

        # Close the connection
        connection_obj.close()

