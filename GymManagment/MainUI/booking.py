from tkinter.constants import CENTER

#from PIL import ImageTk, Image
import tkinter as tk

from tkinter.messagebox import showinfo

from Database.MemberDB import MemberDB
from Database.booking_db import BookingDB
from Database.trainer_db import TrainerDB


# Gui logic
class Booking(tk.Frame):
    title = None
    price = None
    duration = None
    result_box = None
    drop = None
    selected = None
    selectedTrainer = None

    def __init__(self, root):
        db = BookingDB()
        db.create_tables()
        tk.Frame.__init__(self, root)

        root.title("Add Trainer")
        root.geometry("500x200")
        self.db = TrainerDB()
        rows = self.db.get_all_trainers()
        print(rows[0])
        self.selected = tk.StringVar(root)
        self.selected.set('Select Trainer')

        top_heading = tk.Label(self, text="Trainer Booking", fg="black", font=("times new roman", int(20.0)), )
        top_heading.grid(row=0, column=1, columnspan=2)
        self.duration = tk.Entry(self, width=20)

        # Labels for entry forms

        p_duration = tk.Label(self, text="Duration in month ")
        p_drop = tk.Label(self, text="Select Trainer")
        p_duration.grid(row=3, column=0, pady=10)
        p_drop.grid(row=1, column=0, pady=10)
        self.duration.grid(row=3, column=1, padx=5)

        self.drop = tk.OptionMenu(self, self.selected, *rows)
        self.drop.grid(row=1, column=1)

        create = tk.Button(self, text="Book Now", command=self.create)
        back = tk.Button(self, text="Back", command=root.go_main_nav)
        create.grid(row=6, column=1)
        back.grid(row=7, column=1)

    def create(self):
        duration = self.duration.get()
        trainer = self.selected.get()
        print(f'..............Trainer...........${trainer}')
        if not duration:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter duration.")
            return
        else:
            d = BookingDB()
            d.add_booking(trainer, duration)
