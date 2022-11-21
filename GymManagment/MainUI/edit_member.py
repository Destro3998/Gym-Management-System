import tkinter as tk
from tkinter import ttk
import sqlite3 as sq
from tkinter.messagebox import showinfo


class edit_member(tk.Frame):

    username = None

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Edit Member Info")
        root.eval('tk::PlaceWindow . center')
        root.geometry("800x500")
        self.root = root
        top_fram = tk.Frame(self)
        top_fram.grid(pady=0, padx=0)

        user_name = tk.Label(top_fram, text="Enter your Username")

        user_name.grid(row=1, column=1, padx=10, pady=10)

        self.username = tk.Entry(top_fram)
        self.username.grid(row=1, column=2, padx=5, pady=5)

        back = tk.Button(top_fram, text="Back", command=root.go_main_nav)
        back.grid(row=7, column=0, padx=5, pady=5)

        submit = tk.Button(top_fram, text="Submit", command=self.check)
        submit.grid(row=7, column=1, padx=5, pady=5)


    def check(self):
        query = "SELECT * FROM user WHERE username=?"
        conn = sq.connect("Database.db")
        cur = conn.cursor()
        cur.execute(query, (self.username.get(),),)
        rows = cur.fetchone()

        if rows is None:
            showinfo("Unsuccessful", "User with %s does not exist" % self.username.get())
        else:
            self.root.change_page(edit)


class edit(tk.Frame):

    Username = None

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Edit Member Info")
        root.eval('tk::PlaceWindow . center')
        root.geometry("800x500")
        top_fram = tk.Frame(self)
        top_fram.grid(pady=0, padx=0)

        name = tk.Label(top_fram, text="First name")
        last = tk.Label(top_fram, text="Last name")
        email = tk.Label(top_fram, text="Email")
        phone_number = tk.Label(top_fram, text="phone number")
        address = tk.Label(top_fram, text="Address")
        user_name = tk.Label(top_fram, text="Username")

        name.grid(row=1, column=1, padx=10, pady=10)
        last.grid(row=1, column=2, padx=10, pady=10)
        email.grid(row=3, column=0, padx=10, pady=10)
        phone_number.grid(row=3, column=1, padx=10, pady=10)
        address.grid(row=3, column=2, padx=10, pady=10)
        user_name.grid(row=1, column=0, padx=10, pady=10)

        self.first_name = tk.Entry(top_fram)
        self.last_name = tk.Entry(top_fram)
        self.email = tk.Entry(top_fram)
        self.address = tk.Entry(top_fram)
        self.phone_number = tk.Entry(top_fram)
        self.username = tk.Entry(top_fram)

        self.first_name.grid(row=2, column=0, padx=5, pady=5)
        self.last_name.grid(row=2, column=1, padx=5, pady=5)
        self.phone_number.grid(row=2, column=2, padx=5, pady=5)
        self.email.grid(row=4, column=0, padx=5, pady=5)
        self.address.grid(row=4, column=1, padx=5, pady=5)
        self.username.grid(row=4, column=2, padx=5, pady=5)

        back = tk.Button(top_fram, text="Back", command=root.go_main_nav)
        back.grid(row=7, column=0, padx=5, pady=5)

        update = tk.Button(top_fram, text="Update", command=self.update)
        update.grid(row=7, column=1, padx=5, pady=5)

    def update(self):
        if self.first_name.get():
            self.change_first_name(self.first_name.get(), edit_member.username.get())
        elif self.last_name.get():
            self.change_last_name(self.last_name.get(),edit_member.username.get())
        elif self.address.get():
            self.change_address(self.address.get(), edit_member.username.get())
        elif self.phone_number.get():
            self.change_number(self.address.get(), edit_member.username.get())
        elif self.username.get():
            self.change_username(self.username.get(), edit_member.username.get())

    def search_user(self):
        conn = sq.connect("Database.db")
        cur = conn.cursor()
        sqlite_select_query1 = """SELECT * from user where username = ?"""
        cur.execute(sqlite_select_query1, (self.username.get(),))
        user_record = cur.fetchone()

        if user_record is None:
            showinfo("Unsuccessful", "User with that username does not exist")
        else:
            return user_record

    def change_address(self,address, username):
        is_string = True
        query = "UPDATE USER set address = ? WHERE username = ?"
        connection = sq.connect("Database.db")
        cursor = connection.cursor()
        cursor.execute(query, (address, username))
        connection.commit()
        connection.close()

    def change_first_name(self, name, username):
        query = "UPDATE USER set first_name = ? WHERE username = ?"
        connection = sq.connect("Database.db")
        cursor = connection.cursor()
        cursor.execute(query, (name, username))
        connection.commit()
        connection.close()

    def change_last_name(self, name, username):
        query = "UPDATE USER set last_name = ? WHERE username = ?"
        connection = sq.connect("Database.db")
        cursor = connection.cursor()
        cursor.execute(query, (name, username))
        connection.commit()
        connection.close()

    def change_number(self, number, username):
        query = "UPDATE USER set phone_number = ? WHERE username = ?"
        connection = sq.connect("Database.db")
        cursor = connection.cursor()
        cursor.execute(query, (number, username))
        connection.commit()
        connection.close()

    def change_address(self, address, username):
        query = "UPDATE USER set address = ? WHERE username = ?"
        connection = sq.connect("Database.db")
        cursor = connection.cursor()
        cursor.execute(query, (address, username))
        connection.commit()
        connection.close()

    def change_username(self, nusername, username):
        query = "UPDATE USER set username = ? WHERE username = ?"
        connection = sq.connect("Database.db")
        cursor = connection.cursor()
        cursor.execute(query, (nusername, username))
        connection.commit()
        connection.close()

    def get_user_information(self, username):

        """
        gets a specific user information
        :param database: user database for gym system
        :param memberId: integer member id
        :return: the user information
        """
        query = "SELECT * FROM USER WHERE username=?"
        connection = sq.connect("Database.db")
        cursor = connection.cursor()

        cursor.execute(query, [username])
        rows = cursor.fetchone()
        return rows