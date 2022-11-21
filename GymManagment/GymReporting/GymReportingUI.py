# Ariana Fayth Quiambao

import sqlite3

from tkinter import *
import tkinter as tk
from GymReporting.BasicReporting import *

class GymReportingUI(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("About Us")

        # DISPLAY TITLE LABEL
        title = tk.Label(self, text="STAFF AND INSTRUCTORS", bg="#A9A9A9")
        title.grid(row=0, column=0, columnspan=2, pady=30)

        # DISPLAY STAFF
        BasicStaff.get_staff(self)

        plane = []
        for i in range(1, 1 + len(staff)):
            plane.append((0, i))

        flag = 0
        for x, y in plane:
            staffLabel = tk.Label(self, text=staff[flag].staff_specialist + ": " + staff[flag].staff_fname +  " "  +
                                             staff[flag].staff_lname + "\n" + "Contact: " + staff[flag].staff_email +
                                             ", " + staff[flag].staff_address, justify="left")
            flag = flag + 1
            staffLabel.grid(row=y, column=x)

        # DISPLAY TITLE LABEL
        title = tk.Label(self, text="AMENITIES", bg="#A9A9A9")
        title.grid(row=1+len(staff), column=0, columnspan=2, pady=30)

        # DISPLAY AMENITIES
        BasicReporting.get_amenities(self)

        plane = []
        for i in range(2+len(staff), 2+len(staff)+len(amenities)):
            plane.append((0, i))

        flag = 0
        for x, y in plane:
            amenityNameLabel = tk.Label(self, text=amenities[flag].amenity_name, justify="center")
            flag = flag + 1
            amenityNameLabel.grid(row=y, column=x)


        back = tk.Button(self, text="Back", command=root.go_main_nav1)
        back.grid(row=3+len(staff)+len(amenities), column=0, pady=15)

        amenities.clear()
        staff.clear()