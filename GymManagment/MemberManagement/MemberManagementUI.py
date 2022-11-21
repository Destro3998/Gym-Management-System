import re
import sqlite3
import tkinter as tk
import uuid

from tkinter.messagebox import showinfo

from Database.MemberDB import MemberDB

"""
Class for the creation of members, members get added to a database
"""


class MemberManagementUI(tk.Frame):
    first_name = None
    last_name = None
    email = None
    number = None
    address = None
    id = None
    MemberDB = MemberDB()
    MemberDB.create_tables()
    # for validating form entry values
    name_regex = re.compile('[^a-zA-Z]+')
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    address_regex = re.compile('[^0-9a-zA-z ]+')
    number_regex = re.compile('[^0-9]+')

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Member Creation")
        root.geometry("600x500")

        # Entry forms for a basic member object creation

        self.first_name = tk.Entry(self, width=40)
        self.last_name = tk.Entry(self, width=40)
        self.email = tk.Entry(self, width=40)
        self.number = tk.Entry(self, width=40)
        self.address = tk.Entry(self, width=40)

        # Labels for entry forms

        l_first_name = tk.Label(self, text="First Name ")
        l_last_name = tk.Label(self, text="Last Name ")
        l_email = tk.Label(self, text="E-mail ")
        l_number = tk.Label(self, text="Phone Number ")
        l_address = tk.Label(self, text="Address ")

        # Title label for page
        title = tk.Label(self, text="Create A Member", fg="black", font=("times new roman", int(20.0)), pady=10)

        # Button to add member to Dtbf.create(self)
        create = tk.Button(self, text="Create", command=self.create,)
        back = tk.Button(self, text="Back", command=root.go_main_nav,)

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
        back.grid(row=7, column=1, padx=5, pady=15, sticky="ns")

    # Generate a random id, double check that it's not already generated
    # regenerate if it already exists
    def generate_id(self):
        self.id = str(uuid.uuid4())
        if not self.validate_id(self.id):
            self.generate_id()
        else:
            pass

    # Function opens db, adds entry forms to db then closes the db and
    # deletes the forms on the GUI
    def create(self):
        fName = self.first_name.get()
        lastName = self.last_name.get()
        contact = self.number.get()
        email = self.email.get()
        address = self.address.get()
        if not fName:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter FirstName.")
            return
        if not lastName:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter LastName.")
            return
        if not contact:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter Number.")
            return
        if not email:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter Email.")
            return
        if not address:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter Address.")
            return
        # self.generate_id()
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
            d = MemberDB()
            d.add_member(self.first_name.get(), self.last_name.get(), self.email.get(), self.address.get(),
                                self.number.get())

            # Delete the entries once the create button gets pressed

            self.first_name.delete(0, tk.END)
            self.last_name.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.number.delete(0, tk.END)
            self.address.delete(0, tk.END)

            showinfo("Added", "Successfully Added Member")

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

    # function used to double-check whether an id has been assigned already or not
    # function return false if id already exists true if it's a valid id
    def validate_id(self, mem_id):
        conn = sqlite3.connect(r"Database\database.db")
        cur = conn.cursor()
        cur.execute('SELECT * FROM members')
        members = cur.fetchall()
        for x in members:
            if mem_id in x:
                return False
            else:
                return True
