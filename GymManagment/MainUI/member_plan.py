from tkinter.constants import CENTER, END

# from PIL import ImageTk, Image
import tkinter as tk
from tkintertable import TableCanvas
from tkinter.messagebox import showinfo

from Database.MemberDB import MemberDB
from Database.member_plan_db import MemberPlanDB


# Gui logic
class MemberPlan(tk.Frame):
    title = None
    price = None
    duration = None
    result_box = None
    drop = None
    selected = None
    searchMember = None
    fName = None
    lName = None
    email = None
    rows = None

    def __init__(self, root):
        super().__init__()
        root.geometry("600x500")

        self.db = MemberDB()
        self.rows = self.db.get_all_plans()

        if not self.rows:
            self.rows = []
        self.selected = tk.StringVar(root)
        self.selected.set('Select Plans')
        top_heading = tk.Label(self, text="Add Member To Plan", fg="black", font=("times new roman", int(20.0)), )
        top_heading.grid(row=0, column=1, columnspan=1)
        self.title = tk.Entry(self, width=40)
        self.title.focus_set()
        self.fName = tk.Text(self, height=0, width=30, )
        self.fName.grid(row=2, column=1, rowspan=1)
        self.lName = tk.Text(self, height=0, width=30, )
        self.lName.grid(row=3, column=1, rowspan=1)
        self.email = tk.Text(self, height=0, width=30, )
        self.email.grid(row=4, column=1, rowspan=1)
        self.price = tk.Text(self, height=0, width=30, )
        self.duration = tk.Text(self, height=0, width=30, )
        # self.result_box = tk.Entry(self, width=40)

        # Labels for entry forms

        p_title = tk.Label(self, text="Search Member By ID")
        # p_result_box = tk.Label(self, text="Result ")
        p_duration = tk.Label(self, text="Duration ")
        p_price = tk.Label(self, text="Price")
        p_drop = tk.Label(self, text="Select Plans")
        p_fName = tk.Label(self, text="fName")
        p_lName = tk.Label(self, text="lName")
        p_email = tk.Label(self, text="email")
        p_title.grid(row=1, column=0, pady=10)
        # p_result_box.grid(row=2, column=0, pady=10)
        p_duration.grid(row=6, column=0, pady=10)
        p_price.grid(row=7, column=0, pady=10)
        p_drop.grid(row=5, column=0, pady=10)
        p_fName.grid(row=2, column=0, pady=10)
        p_lName.grid(row=3, column=0, pady=10)
        p_email.grid(row=4, column=0, pady=10)
        self.title.grid(row=1, column=1, padx=5)
        # self.result_box.grid(row=2, column=1, padx=5)
        self.duration.grid(row=6, column=1, padx=5)
        self.price.grid(row=7, column=1, padx=5)

        self.drop = tk.OptionMenu(self, self.selected, *self.rows, command=self.search_plans)
        self.drop.grid(row=5, column=1)

        create = tk.Button(self, text="Add", command=self.create, width=20
                           )
        back = tk.Button(self, text="Back", command=root.go_main_nav1, width=5)
        search = tk.Button(self, text="Search", command=self.btn_clicked, width=5)
        create.grid(row=8, column=1, columnspan=2, pady=15)
        back.grid(row=8, column=0, padx=5, pady=15, sticky="ns")
        search.grid(row=1, column=3, padx=5, sticky="w")

    def create(self):
        memebr_id = self.title.get()
        duration = self.duration
        price = self.price
        selectedPlan = self.selected.get()

        if not price:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter Price.")
            return
        if not duration:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter duration.")
            return
        if not selectedPlan:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please select plan.")
            return
        else:
            db = MemberPlanDB()
            db.create_memeber_plan(memebr_id, selectedPlan, price, duration)

    def btn_clicked(self):
        # result = self.result_box.get()
        # if not result:
        #     tk.messagebox.showerror(
        #         title="Empty Fields!", message="Please enter member Id.")
        #     return
        self.search_member()

    def search_member(self):
        result = self.title.get()
        if not result:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter member Id.")
            return
        else:
            self.searchMember = self.db.get_member_by_id(self.title.get())
            self.fName.insert(END, self.searchMember[1])
            self.lName.insert(END, self.searchMember[2])
            self.email.insert(END, self.searchMember[3])
            print(self.searchMember)

    def search_plans(self, value):
        print(f'.............ID...........{value[0]}')
        self.searchMember = self.db.get_plans_by_id(value[0])
        self.duration.insert(END, self.searchMember[4])
        self.price.insert(END, self.searchMember[2])
        print(self.searchMember)
