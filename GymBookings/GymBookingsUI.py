# Ariana Fayth Quiambao

import sqlite3

import tkinter as tk
from tkinter.messagebox import showinfo

from GymBookings.BasicBooking import *
from GymBookings.BookingsTest import *
from Database import dbbookings

class GymBookingsUI(tk.Frame):

    classID = None

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Classes")

        # DISPLAY TITLE LABEL
        title = tk.Label(self, text="Book A Class")
        title.grid(row=0, column=0, columnspan=2, pady=30)

        # DISPLAY LABEL FOR ENTRY BOX
        l_classIDbox = tk.Label(self, text="Enter Class ID: ")
        l_classIDbox.grid(row=1, column=0, pady=10)

        # DISPLAY ENTRY BOX FOR CLASS ID
        self.classID = tk.Entry(self)
        self.classID.grid(row=1, column=1, padx=5)

        # DISPLAY BUTTONS TO SIGN UP FOR AND WITHDRAW FROM CLASSES
        b_signUp = tk.Button(self, text="Sign Up", command=self.signup)
        b_signUp.grid(row=1, column=2)
        b_withdraw = tk.Button(self, text="Withdraw", command=self.withdraw)
        b_withdraw.grid(row=1, column=3)

        # DISPLAY HEADER LABELS
        l_classID = tk.Label(self, text="Class ID: ")
        l_classID.grid(row=2, column=0, pady=10)
        l_class = tk.Label(self, text="Class: ")
        l_class.grid(row=2, column=1, pady=10)
        l_time = tk.Label(self, text="Time: ")
        l_time.grid(row=2, column=2, padx=5)

        # DISPLAY CLASS IDS OF AVAILABLE CLASSES
        plane = []
        for i in range(3, 2 + len(bookings)):
            plane.append((0, i))

        flag = 0
        for x, y in plane:
            # Button to add member to Dtb
            signUp = tk.Label(self, text=bookings[flag].classID)
            flag = flag + 1
            signUp.grid(row=y, column=x)

        # DISPLAY NAMES OF AVAILABLE CLASSES
        plane = []
        for i in range(3, 2 + len(bookings)):
            plane.append((1, i))

        flag = 0
        for x, y in plane:
            # Button to add member to Dtb
            signUp = tk.Label(self, text=bookings[flag].class_name)
            flag = flag + 1
            signUp.grid(row=y, column=x)

        # DISPLAY TIME SLOTS OF AVAILABLE CLASSES
        plane = []
        for i in range(3, 2 + len(bookings)):
            plane.append((2, i))

        flag = 0
        for x, y in plane:
            # Button to add member to Dtb
            signUp = tk.Label(self, text=bookings[flag].class_timeslot)
            flag = flag + 1
            signUp.grid(row=y, column=x)

        back = tk.Button(self, text="Back", command=root.go_main_nav)
        back.grid(row=3 + len(bookings), column=0, pady=15)

    def signup(self):

        # if condition for when class does not exist
        found = "no"
        for x in bookings:
            if self.classID.get() == x.classID:
                found = "yes"
                break

        if found == "no":
            showinfo("Unuccessful!", "Class does not exist!")
            return

        # Connecting to sqlite
        connection_obj = sqlite3.connect(r'C:\Users\maxie\Downloads\cmpt370-MembyManagement\cmpt370-MembyManagement\Database\database.db')
        # cursor object
        cursor_obj = connection_obj.cursor()

        # retrieve past bookings
        sqlite_select_query = """SELECT * from USERS where username = ?"""
        cursor_obj.execute(sqlite_select_query, (testUser,))
        record = cursor_obj.fetchone()

        # setup if condition for when class is already booked
        if record[10].find('[' + self.classID.get() + ']') != -1:
            connection_obj.close()
            showinfo("Unuccessful!", "Already Signed Up to Class!")
            return

        # past bookings + recently signed up booking
        classIDflag = record[10] + '[' + self.classID.get() + ']'
        cursor_obj.execute('UPDATE USERS SET Bookings=? WHERE username=?', (classIDflag, testUser))

        # Commit your changes in the database
        connection_obj.commit()
        # Closing the connection
        connection_obj.close()

        # show a popup stating successful signup
        showinfo("Successful!", "Signed Up to Class!")

        # cler entry box
        self.classID.delete(0, tk.END)


    def withdraw(self):

        # if condition for when class does not exist
        found = "no"
        for x in bookings:
            if self.classID.get() == x.classID:
                found = "yes"
                break

        if found == "no":
            showinfo("Unuccessful!", "Class does not exist!")
            return

        # Connecting to sqlite
        connection_obj = sqlite3.connect(r'C:\Users\maxie\Downloads\cmpt370-MembyManagement\cmpt370-MembyManagement\Database\database.db')

        # cursor object
        cursor_obj = connection_obj.cursor()

        # retrieve past bookings
        sqlite_select_query = """SELECT * from USERS where username = ?"""
        cursor_obj.execute(sqlite_select_query, (testUser,))
        record = cursor_obj.fetchone()

        # setup if condition for when class is not signed up to
        if record[10].find('[' + self.classID.get() + ']') == -1:
            connection_obj.close()
            showinfo("Unuccessful!", "Not Signed Up to Class!")
            return

        # delete selected booking from past bookings
        search = '[' + self.classID.get() + ']'
        classIDflag = record[10]
        classIDflag = classIDflag.replace(search, '')
        cursor_obj.execute('UPDATE USERS SET Bookings=? WHERE username=?', (classIDflag, testUser))

        # Commit your changes in the database
        connection_obj.commit()
        # Closing the connection
        connection_obj.close()

        # show a popup stating successful withdrawal
        showinfo("Successful!", "Withdrew from Class!")

        # cler entry box
        self.classID.delete(0, tk.END)
