# Damon Dix

import tkinter as tk

"""

"""


class MemberManagementUI(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Member Creation")

        # Entry forms for a basic member object creation

        first_name = tk.Entry(self)
        last_name = tk.Entry(self)
        email = tk.Entry(self)
        number = tk.Entry(self)
        address = tk.Entry(self)

        # Labels for entry forms

        l_first_name = tk.Label(self, text="First Name: ")
        l_last_name = tk.Label(self, text="Last Name: ")
        l_email = tk.Label(self, text="E-mail: ")
        l_number = tk.Label(self, text="Phone Number: ")
        l_address = tk.Label(self, text="Address: ")

        # Title label for page
        title = tk.Label(self, text="Create A Member")

        # Button to add member to Dtb
        create = tk.Button(self, text="Create")

        # place everything in a grid for organization and view

        title.grid(row=0, column=0, columnspan=2, pady=30)
        l_first_name.grid(row=1, column=0, pady=10)
        l_last_name.grid(row=2, column=0, pady=10)
        l_email.grid(row=3, column=0, pady=10)
        l_number.grid(row=4, column=0, pady=10)
        l_address.grid(row=5, column=0, pady=10)
<<<<<<< HEAD
=======

>>>>>>> GymBookings
        first_name.grid(row=1, column=1, padx=5)
        last_name.grid(row=2, column=1, padx=5)
        email.grid(row=3, column=1, padx=5)
        number.grid(row=4, column=1, padx=5)
        address.grid(row=5, column=1, padx=5)
<<<<<<< HEAD
=======

>>>>>>> GymBookings
        create.grid(row=6, column=0, columnspan=2, pady=15)

