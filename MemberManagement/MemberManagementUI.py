# Damon Dix

import tkinter as tk
import sqlite3
from Database import MemberDB

"""
Class for the creation of members, members get added to a database
"""


class MemberManagementUI(tk.Frame):
    first_name = ""
    last_name = ""
    email = ""
    number = 0
    address = ""
    MemberDB = MemberDB.MemberDB()

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Member Creation")

        # Entry forms for a basic member object creation

        self.first_name = tk.Entry(self)
        self.last_name = tk.Entry(self)
        self.email = tk.Entry(self)
        self.number = tk.Entry(self)
        self.address = tk.Entry(self)

        # Labels for entry forms

        l_first_name = tk.Label(self, text="First Name: ")
        l_last_name = tk.Label(self, text="Last Name: ")
        l_email = tk.Label(self, text="E-mail: ")
        l_number = tk.Label(self, text="Phone Number: ")
        l_address = tk.Label(self, text="Address: ")

        # Title label for page
        title = tk.Label(self, text="Create A Member")

        # Button to add member to Dtbf.create(self)
        create = tk.Button(self, text="Create", command=self.create)
        back = tk.Button(self, text="Back", command=root.go_main_nav)

        # place everything in a grid for organization and view

        title.grid(row=0, column=0, columnspan=2, pady=30)
        l_first_name.grid(row=1, column=0, pady=10)
        l_last_name.grid(row=2, column=0, pady=10)
        l_email.grid(row=3, column=0, pady=10)
        l_number.grid(row=4, column=0, pady=10)
        l_address.grid(row=5, column=0, pady=10)

        self.first_name.grid(row=1, column=1, padx=5)
        self.last_name.grid(row=2, column=1, padx=5)
        self.email.grid(row=3, column=1, padx=5)
        self.number.grid(row=4, column=1, padx=5)
        self.address.grid(row=5, column=1, padx=5)

        create.grid(row=6, column=1, columnspan=2, pady=15)
        back.grid(row=6, column=0, pady=15)

    # Function opens db, adds entry forms to db then closes the db and
    # deletes the forms on the GUI
    def create(self):
        conn = sqlite3.connect("members.db")
        cur = conn.cursor()

        # Insert entries into the table
        cur.execute("INSERT INTO members VALUES (:first_name, :last_name, :email, :number, :address)",
                    {
                        'first_name': self.first_name.get(),
                        'last_name': self.last_name.get(),
                        'email': self.email.get(),
                        'number': self.email.get(),
                        'address': self.address.get()})

        conn.commit()

        conn.close()

        # Delete the entries once the create button gets pressed

        self.first_name.delete(0, tk.END)
        self.last_name.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.number.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.show_db()

    # For testing purposes, data will show upon exiting the application
    def show_db(self):
        conn = sqlite3.connect('members.db')
        cur = conn.cursor()

        cur.execute("SELECT *, oid FROM members")
        entries = cur.fetchall()
        print(entries)
