import sqlite3

import tkinter as tk
from tkinter.messagebox import showinfo

from cmpt370.Equipments.EqupimentsClass import *


class EquipmentsUI(tk.Frame):
    classID = None

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.enter = None
        root.title("Equipments")

        # DISPLAY TITLE LABEL
        title = tk.Label(self, text="Select Equipment Category")
        title.grid(row=0, column=0, columnspan=3, pady=30)

        # DISPLAY LABEL FOR ENTRY BOX
        l_classIDbox = tk.Label(self, text="Enter Category ID: ")
        l_classIDbox.grid(row=1, column=0, pady=10)

        # DISPLAY ENTRY BOX FOR CLASS ID
        self.classID = tk.Entry(self)
        self.classID.grid(row=1, column=1, padx=5)

        # DISPLAY BUTTONS TO SIGN UP FOR AND WITHDRAW FROM CLASSES
        E_enter = tk.Button(self, text="Enter", command=self.enter)
        E_enter.grid(row=1, column=2)

        # DISPLAY HEADER LABELS
        l_classID = tk.Label(self, text="Category ID: ")
        l_classID.grid(row=2, column=0, pady=10)
        l_class = tk.Label(self, text="Equipments Category: ")
        l_class.grid(row=2, column=1, pady=10)

        # DISPLAY CLASS IDS OF AVAILABLE CLASSES
        plane = []
        for i in range(3, 2 + len(equipments)):
            plane.append((0, i))

        flag = 0
        for x, y in plane:
            # Button to add member to Dtb
            signUp = tk.Label(self, text=equipments[flag].classID)
            flag = flag + 1
            signUp.grid(row=y, column=x)

        # DISPLAY NAMES OF AVAILABLE CLASSES
        plane = []
        for i in range(3, 2 + len(equipments)):
            plane.append((1, i))

        flag = 0
        for x, y in plane:
            # Button to add member to Dtb
            signUp = tk.Label(self, text=equipments[flag].class_name)
            flag = flag + 1
            signUp.grid(row=y, column=x)

        back = tk.Button(self, text="Back", command=root.go_main_nav)
        back.grid(row=3 + len(equipments), column=0, pady=15)

    def enter(self):

        # if condition for when class does not exist
        found = "no"
        for x in equipments:
            if self.classID.get() == x.classID:
                found = "yes"
                break

        if found == "no":
            showinfo("Unuccessful!", "Class does not exist!")
            return

        # Connecting to sqlite
        connection = sqlite3.connect(
            r'C:\Users\maxie\Downloads\cmpt370-MembyManagement\cmpt370-MembyManagement\Database\database.db')
        # cursor object
        cursor_obj = connection.cursor()

        connection.commit()
        # Closing the connection
        connection.close()




