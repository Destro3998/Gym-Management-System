
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
class TimeSlots(tk.Frame):

    def __init__(self,root):
        tk.Frame.__init__(self, root)
        root.title("Gym Time slots")
        self.title = None
        self.start_time = None
        self.end_time = None
        self.day = None
        self.id = None

        self.db=timeSlotDB()
        self.db.create_tables()
        root.geometry("800x500")
        root.title("Welcome")
        top_fram = tk.Frame(self)

        top_fram.pack()
        data_from = tk.Frame(self)

        data_from.pack()
        top_heading = tk.Label(top_fram, text="Add Classes", fg="black", font=("times new roman", int(20.0)), )
        top_heading.grid(row=0, column=1, columnspan=2)
        self.title = tk.Entry(top_fram, width=40)
        self.title.focus_set()
        self.start_time = tk.Entry(top_fram, width=40)
        self.end_time = tk.Entry(top_fram, width=40)
        self.day = tk.Entry(top_fram, width=40)

        # Labels for entry forms

        p_title = tk.Label(top_fram, text="Class Name")
        s_time = tk.Label(top_fram, text="Start Time of slot(24 hour format)")
        s_rime = tk.Label(top_fram, text="End time of slot(24 hour format) ")
        day_l = tk.Label(top_fram, text="Day")
        p_title.grid(row=1, column=0, pady=10)
        s_time.grid(row=2, column=0, pady=10)
        s_rime.grid(row=3, column=0, pady=10)
        day_l.grid(row=4, column=0, pady=10)

        self.title.grid(row=1, column=1, padx=5)
        self.start_time.grid(row=2, column=1, padx=5)
        self.end_time.grid(row=3, column=1, padx=5)
        self.day.grid(row=4, column=1, padx=5)

        create = tk.Button(top_fram, text="Add Time Slot", command=self.create, width=20)
        back = tk.Button(top_fram,  text="Back", command=root.go_main_nav1, width=5)
        create.grid(row=6, column=1, columnspan=2, pady=15)

        back.grid(row=6, column=0, padx=5, pady=15, sticky="ns")
        self.table = TableCanvas(data_from,
                    thefont=('Arial',15),rowheight=25,
                    rowselectedcolor='gray',read_only=True,rows=0,cols=0)

        self.table.show()
        self.get_time_slot()

    def get_time_slot(self):
        lst = self.db.get_time_slots()
        model = self.table.model
        self.table.cols=4
        model.importDict(lst)
        self.table.redraw()

    def create(self):
        title = self.title.get()
        start_time = self.start_time.get()
        end_time = self.end_time.get()
        day_entry = self.day.get()
        if not title:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter Class Name.")
            return
        if not start_time:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Start Time is required")
            return
        if not end_time:
            tk.messagebox.showerror(
                title="Empty Fields!", message="End time is required")
            return
        if len(start_time)>6 or len(start_time)<3:
            tk.messagebox.showerror(
                title="Wrong input", message="Please Enter valid start time like 12:23")
            return

        if len(end_time)>5 or len(end_time)<3:
            tk.messagebox.showerror(
                title="Wrong input", message="Please Enter valid end time like 12:23")
            return
        if ":" not in start_time or ":" not in end_time or "am" in start_time or "pm" in end_time:
            tk.messagebox.showerror(
                title="Wrong input", message="Please Enter valid end time like 21:23 without am or pm")
            return
        if int(start_time[:2]) >24 and int(end_time[:2]) >24:
            tk.messagebox.showerror(
                title="Wrong input", message="Please Enter valid time,hours must be less then 24")
            return
        if int(start_time[:2] )> int(end_time[:2]):
            tk.messagebox.showerror(
                title="Wrong input", message="End time must be greater then start time")
            return

        flag=self.db.create_time_slots(title,start_time,end_time, day_entry)
        if flag:
            self.get_time_slot()
            self.title.delete(0, tk.END)
            self.start_time.delete(0, tk.END)
            self.end_time.delete(0, tk.END)
            self.day.delete(0, tk.END)
        else:
            tk.messagebox.showerror(
                title="Error", message="Error during insertion in database")
            return

