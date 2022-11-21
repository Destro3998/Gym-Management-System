
import sqlite3

import tkinter as tk
from tkinter.messagebox import showinfo
from tkintertable import TableCanvas, TableModel
from Database.time_slots_db import timeSlotDB
class GymBookingsUI(tk.Frame):

    classID = None

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Classes")
        root.geometry("700x500")
        self.db = timeSlotDB()
        top_fram = tk.Frame(self)
        top_fram.pack()

        data_from = tk.Frame(self)
        data_from.pack()
        # DISPLAY TITLE LABEL
        title = tk.Label(top_fram, text="SignUp/Withdraw ",  fg="black", font=("Arial", 25), pady=10)
        title.grid(row=0, column=1, columnspan=2, pady=0)

        # DISPLAY LABEL FOR ENTRY BOX
        l_classIDbox = tk.Label(top_fram, text="Enter Class ID ")
        l_classIDbox.grid(row=1, column=0, pady=10)

        l_user = tk.Label(top_fram, text="Enter Username")
        l_user.grid(row=2, column=0, pady=10)

        # DISPLAY ENTRY BOX FOR CLASS ID
        self.classID = tk.Entry(top_fram, width=40)
        self.classID.focus_set()
        self.classID.grid(row=1, column=1, padx=5)

        self.user = tk.Entry(top_fram, width=40)
        self.user.focus_set()
        self.user.grid(row=2, column=1)

        # DISPLAY BUTTONS TO SIGN UP FOR AND WITHDRAW FROM CLASSES
        b_signUp = tk.Button(top_fram, text="Sign Up", command=self.signup,)
        b_signUp.grid(row=1, column=2)
        b_withdraw = tk.Button(top_fram, text="Withdraw", command=self.withdraw,)
        b_withdraw.grid(row=1, column=3)

        back = tk.Button(data_from, text="Back", command=root.go_main_nav,)
        back.grid(row=2, column=1, pady=15)


        self.table = TableCanvas(data_from,thefont=('Arial', 15), rowheight=25,
                                 rowselectedcolor='gray', read_only=True, rows=0, cols=0)

        self.table.show()
        self.get_time_slot()

    def get_time_slot(self):
        lst = self.db.get_time_slots()
        model = self.table.model
        self.table.cols = 4
        model.importDict(lst)
        self.table.redraw()

    def signup(self):

        # Connecting to sqlite
        connection_obj = sqlite3.connect("../MainUI/Database.db")
        # cursor object
        cursor_obj = connection_obj.cursor()

        sqlite_select_query1 = """SELECT * from classes where id = ?"""
        cursor_obj.execute(sqlite_select_query1, (self.classID.get(),))
        class_record = cursor_obj.fetchone()

        if class_record is None:
            showinfo("Unsuccessful", "Class with that id does not exist")

        # retrieve past bookings
        sqlite_select_query = """SELECT * from USER where username = ?"""
        cursor_obj.execute(sqlite_select_query, (self.user.get(),))
        record = cursor_obj.fetchone()

        if record is None:
            showinfo("Unsuccessful", "Username does not exist")
        print(record)

        # setup if condition for when class is already booked
        if record[9] is None:
            classIDflag = '[' + self.classID.get() + ']'
            cursor_obj.execute('UPDATE USER SET Bookings=? WHERE username=?', (classIDflag, self.user.get()))

        elif record[9].find('[' + self.classID.get() + ']') != -1:
            connection_obj.close()
            showinfo("Unuccessful!", "Already Signed Up to Class!")
            return

        else:
            classIDflag = record[9] + '[' + self.classID.get() + ']'
            cursor_obj.execute('UPDATE USER SET Bookings=? WHERE username=?', (classIDflag, self.user.get()))

        # Commit your changes in the database
        connection_obj.commit()
        # Closing the connection
        connection_obj.close()

        # show a popup stating successful signup
        showinfo("Successful!", "Signed Up to Class!")

        # cler entry box
        self.classID.delete(0, tk.END)

    def withdraw(self):

        # Connecting to sqlite
        connection_obj = sqlite3.connect(r'database.db')

        # cursor object
        cursor_obj = connection_obj.cursor()

        sqlite_select_query1 = """SELECT * from classes where id = ?"""
        cursor_obj.execute(sqlite_select_query1, (self.classID.get(),))
        class_record = cursor_obj.fetchone()

        if class_record is None:
            showinfo("Unsuccessful", "Class with that id does not exist")

        sqlite_select_query = """SELECT * from USER where username = ?"""
        cursor_obj.execute(sqlite_select_query, (self.user.get(),))
        record = cursor_obj.fetchone()

        if record is None:
            showinfo("Unsuccessful", "Username does not exist")

        # setup if condition for when class is not signed up to
        if record[9].find('[' + self.classID.get() + ']') == -1:
            connection_obj.close()
            showinfo("Unuccessful!", "Not Signed Up to Class!")
            return

        # delete selected booking from past bookings
        search = '[' + self.classID.get() + ']'
        classIDflag = record[9]
        classIDflag = classIDflag.replace(search, '')
        cursor_obj.execute('UPDATE USER SET Bookings=? WHERE username=?', (classIDflag, self.user.get()))

        # Commit your changes in the database
        connection_obj.commit()
        # Closing the connection
        connection_obj.close()

        # show a popup stating successful withdrawal
        showinfo("Successful!", "Withdrew from Class!")

        # cler entry box
        self.classID.delete(0, tk.END)

    def get_time_slots(self):
        try:
            conn = sqlite3.connect("../MainUI/Database.db")
            cur = conn.cursor()
            res = cur.execute("""SELECT * FROM classes""")
            data_1 = cur.fetchall()
            conn.commit()
            conn.close()
            dict = {}
            for i, d in enumerate(data_1):
                dict[i] = d
            return dict
        except Exception as ex:
            print(ex)
            return []
