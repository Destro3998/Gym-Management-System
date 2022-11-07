# Damon Dix
import re
import tkinter as tk
import sqlite3
from tkinter.messagebox import showinfo

from Database import MemberDB

"""
Class for the creation of members, members get added to a database
"""


class MemberManagementUI(tk.Frame):
    first_name = None
    last_name = None
    email = None
    number = None
    address = None
    MemberDB = MemberDB.MemberDB()

    # for validating form entry values
    name_regex = re.compile('[^a-zA-Z]+')
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    address_regex = re.compile('[^0-9a-zA-z ]+')
    number_regex = re.compile('[^0-9]+')

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

        # if any of the input fields are empty print message
        if [x for x in (self.first_name, self.last_name, self.email, self.address, self.number) if x is None]:
            showinfo("Missing Items", "Error \nPlease make sure you fill out all required fields")
        elif not self.validate_f_name():
            showinfo("Incorrect Format", "First name must be < 20 characters and not contain any numbers, symbols or "
                                         "spaces")
        elif not self.validate_l_name():
            showinfo("Incorrect Format", "Last name must be < 30 characters and not contain any numbers, symbols or "
                                         "spaces")
        elif not self.validate_email():
            showinfo("Incorrect Format", "Not a valid email, must be in abc123@abs123.abd format")
        elif not self.validate_number():
            showinfo("Incorrect Format", "Not a valid phone number, must only contain numbers and be 10 numbers long")
        elif not self.validate_address():
            showinfo("Incorrect format", "Address must not contain any symbols, only numbers and letters")
        else:

            conn = sqlite3.connect("members.db")
            cur = conn.cursor()
            print("whoops added")
            val = self.validate_email()
            # print (str(val))

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

    # validation functions fo entries
    def validate_f_name(self):
        if len(self.first_name.get()) > 20:
            return False
        elif self.name_regex.search(self.first_name.get()):
            return False
        else:
            return True

    def validate_l_name(self):
        if len(self.last_name.get()) > 20:
            return False
        elif self.name_regex.search(self.last_name.get()):
            return False
        else:
            return True

    def validate_email(self):
        if not self.email_regex.search(self.email.get()):
            return False
        else:
            return True

    def validate_address(self):
        if self.address_regex.search(self.address.get()):
            return False
        else:
            return True

    def validate_number(self):
        if len(self.number.get()) != 10:
            return False
        elif self.number_regex.search(self.number.get()):
            return False
        else:
            return True
