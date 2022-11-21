from tkinter.constants import CENTER

from PIL import ImageTk, Image
import tkinter as tk

from tkinter.messagebox import showinfo

from Database.time_slots_db import timeSlotDB
from tkintertable import TableCanvas, TableModel

status_list = [
    'Active',
    'Inactive',
    'Expired',
    'Pending'
]


# Gui logic
class UpdateTime(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Gym Time slots")
        self.title = None
        self.start_time = None
        self.end_time = None

        self.db = timeSlotDB()
        self.db.create_tables()
        root.geometry("800x400")
        root.minsize(800, 400)
        root.maxsize(800, 400)
        root.title("Welcome")
        top_heading = tk.Label(self, text="Update Gym Time", fg="black", font=("times new roman", int(20.0)), )
        top_heading.grid(row=0, column=1, columnspan=2)
        self.title = tk.Entry(self, width=40)
        self.title.focus_set()
        self.start_time = tk.Entry(self, width=40)
        self.end_time = tk.Entry(self, width=40)

        # self.status = tk.Combobox(self, font=("times new roman", 13), state='readonly', justify=CENTER)

        # Labels for entry forms

        s_time = tk.Label(self, text="Start Time of slot(24 hour format)")
        s_rime = tk.Label(self, text="End time of slot(24 hour format) ")
        s_time.grid(row=2, column=0, pady=10)
        s_rime.grid(row=3, column=0, pady=10)

        self.start_time.grid(row=2, column=1, padx=5)
        self.end_time.grid(row=3, column=1, padx=5)

        create = tk.Button(self, text="Add Time Slot", command=self.create, width=20)
        back = tk.Button(self, text="Back", command=root.go_main_nav, width=5)
        create.grid(row=6, column=1, columnspan=2, pady=15)

        back.grid(row=6, column=0, padx=5, pady=15, sticky="ns")

    def create(self):
        start_time = self.start_time.get()
        end_time = self.end_time.get()
        if not start_time:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Start Time is required")
            return
        if not end_time:
            tk.messagebox.showerror(
                title="Empty Fields!", message="End time is required")
            return
        if len(start_time) > 5 or len(start_time) < 3:
            tk.messagebox.showerror(
                title="Wrong input", message="Please Enter valid start time like 12:23")
            return

        if len(end_time) > 5 or len(end_time) < 3:
            tk.messagebox.showerror(
                title="Wrong input", message="Please Enter valid end time like 12:23")
            return
        if ":" not in start_time or ":" not in end_time or "am" in start_time or "pm" in end_time:
            tk.messagebox.showerror(
                title="Wrong input", message="Please Enter valid end time like 21:23 without am or pm")
            return
        if int(start_time[:2]) > 24 and int(end_time[:2]) > 24:
            tk.messagebox.showerror(
                title="Wrong input", message="Please Enter valid time,hours must be less then 24")
            return
        if int(start_time[:2]) > int(end_time[:2]):
            tk.messagebox.showerror(
                title="Wrong input", message="End time must be greater then start time")
            return
        else:
            self.db.update_time(start_time, end_time)
            tk.messagebox.showerror(
                title="Error", message="Error during insertion in database")
        return
