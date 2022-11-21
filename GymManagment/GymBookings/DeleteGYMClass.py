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
class DeleteClass(tk.Frame):

    def __init__(self,root):
        tk.Frame.__init__(self, root)
        root.title("Gym Time slots")
        self.id = None

        self.db=timeSlotDB()
        self.db.create_tables()
        root.geometry("800x500")
        root.title("Welcome")
        top_fram = tk.Frame(self)

        top_fram.pack()
        data_from = tk.Frame(self)

        data_from.pack()
        top_heading = tk.Label(top_fram, text="Delete classes", fg="black", font=("times new roman", int(20.0)), )
        top_heading.grid(row=0, column=1, columnspan=2)
        self.id = tk.Entry(top_fram, width=40)
        self.id.focus_set()


        # Labels for entry forms

        p_id = tk.Label(top_fram, text="Class Name")
        p_id.grid(row=1, column=0, pady=10)

        self.id.grid(row=1, column=1, padx=5)

        delete = tk.Button(top_fram, text="Delete Class", command=self.deleteclass, width=20)
        back = tk.Button(top_fram,  text="Back", command=root.go_main_nav1, width=5)
        delete.grid(row=6, column=1, columnspan=2, pady=15)

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

    def deleteclass(self):
        id = self.id.get()

        if not id:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter Class Name.")
            return
        if id.isdigit() is not True:
            tk.messagebox.showerror(
                title="Wrong input", message="Please Enter valid id")
            return
        flag = self.db.delete_class(id)
        if flag:
            tk.messagebox.showerror(
                title="Error", message="Error during deletion from database")
            return
        else:
            self.get_time_slot()
            showinfo("Successful", "Deleted class successfully")