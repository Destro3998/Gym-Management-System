from tkinter.constants import CENTER


# from PIL import ImageTk, Image
import tkinter as tk

from tkinter.messagebox import showinfo

from Database.plan_db import PlanDB

status_list = [
    'Active',
    'Inactive',
    'Expired',
    'Pending'
]


# Gui logic
class Plan(tk.Frame):

    def __init__(self,root):
        tk.Frame.__init__(self, root)
        root.title("Search Member")
        self.title = None
        self.price = None
        self.duration = None
        self.status = None
        db = PlanDB()
        db.create_tables()
        root.geometry("600x500")
        root.minsize(200, 400)
        root.maxsize( 800, 400)
        #root.title("Create plan")
        top_heading = tk.Label(self, text="Create Plan", fg="black", font=("times new roman", int(20.0)), )
        top_heading.grid(row=0, column=1, columnspan=2)
        self.title = tk.Entry(self, width=40)
        self.title.focus_set()
        self.price = tk.Entry(self, width=40)
        self.duration = tk.Entry(self, width=40)
        self.status = tk.Entry(self, width=40)
        # self.status = tk.Combobox(self, font=("times new roman", 13), state='readonly', justify=CENTER)

        # Labels for entry forms

        p_title = tk.Label(self, text="Title ")
        p_price = tk.Label(self, text="Price ")
        p_duration = tk.Label(self, text="Duration ")
        p_status = tk.Label(self, text="Status ")
        p_title.grid(row=1, column=0, pady=10)
        p_price.grid(row=2, column=0, pady=10)
        p_duration.grid(row=3, column=0, pady=10)
        p_status.grid(row=4, column=0, pady=10)
        self.title.grid(row=1, column=1, padx=5)
        self.price.grid(row=2, column=1, padx=5)
        self.duration.grid(row=3, column=1, padx=5)
        self.status.grid(row=4, column=1, padx=5)

        create = tk.Button(self, text="Create", command=self.create, width=20,)
        #back = tk.Button(self, text="Back", width=5)
        back = tk.Button(self, text="Back", command=root.go_main_nav1, width=5,)
        create.grid(row=6, column=1, columnspan=2, pady=15)
        back.grid(row=6, column=0, padx=5, pady=15, sticky="ns")

    def create(self):
        title = self.title.get()
        price = self.price.get()
        duration = self.duration.get()
        status = self.status.get()

        if not title:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter Title.")
            return
        if not price:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter Price.")
            return
        if not duration:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter duration.")
            return
        if not status:
            status = "Active"

        db=PlanDB()

        flag=db.create_plan(title,price,duration,status)
        if flag:
            tk.messagebox.showinfo(
                title="Record Added", message="New Plan is stored in Database")
            return
        else:
            tk.messagebox.showerror(
                title="Error", message="Error during insertion in database")
            return


