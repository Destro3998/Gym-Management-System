from tkinter.constants import CENTER

# from PIL import ImageTk, Image
import tkinter as tk

from tkinter.messagebox import showinfo

from Database.equipment_db import EquipmentDB
from tkintertable import TableCanvas, TableModel
from tkinter import filedialog


# Gui logic
class Equipments(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Equipment")
        self.title = None
        self.desc = None

        self.db = EquipmentDB()
        self.db.create_tables()
        root.geometry("800x500")


        top_fram = tk.Frame(self)

        top_fram.pack()
        data_from = tk.Frame(self)

        data_from.pack()
        top_heading = tk.Label(top_fram, text="Create Equipment", font=("times new roman", int(20.0)), )
        top_heading.grid(row=0, column=1, columnspan=2)

        self.title = tk.Entry(top_fram, width=40)
        self.title.focus_set()
        self.desc = tk.Entry(top_fram, width=40)

        # Labels for entry forms

        p_title = tk.Label(top_fram, text="Equipment Name")
        desc = tk.Label(top_fram, text="Description")


        p_title.grid(row=1, column=0, pady=10)
        desc.grid(row=2, column=0, pady=10)

        self.title.grid(row=1, column=1, padx=5)
        self.desc.grid(row=2, column=1, padx=5)

        create = tk.Button(top_fram, text="add Equipments", command=self.create, width=20)
        h = tk.Scrollbar(data_from)

        data = self.db.get_equipments()

        print(data)
        data_fram = tk.Frame(data_from, background="red")
        data_fram.grid(row=1, column=0, rowspan=112)

        back = tk.Button(data_from, text="Back", command=root.go_main_nav1, width=5)
        create.grid(row=5, column=1)

        back.grid(row=6, column=1)

    def get_time_slot(self):

        lst = self.db.get_time_slots()
        print(lst)
        model = self.table.model
        self.table.cols = 4
        model.importDict(lst)
        self.table.redraw()

    def create(self):
        title = self.title.get()
        desc = self.desc.get()

        flag = self.db.add_equipments(title, desc)
        if flag:
            self.title.delete(0, tk.END)
            self.desc.delete(0, tk.END)
            pass
        else:
            tk.messagebox.showerror(
                title="Error", message="Error during insertion in database")
            return
