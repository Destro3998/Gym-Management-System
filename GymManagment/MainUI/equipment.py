import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Database.equipment_db import EquipmentDB


class show_equiments(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("View Equipment")

        self.db = EquipmentDB()
        root.geometry("800x500")
        top_fram = tk.Frame(self)
        top_fram.pack()

        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        row = cur.execute("SELECT * FROM equipments")
        rows = row.fetchall()

        columns = ('Equipment name', 'Description',)
        tree = ttk.Treeview(top_fram, columns=columns, show='headings', )

        back = tk.Button(self, text="Back", command=root.go_main_nav)
        back.pack()

        # define headings
        tree.heading('Equipment name', text='Equipment Name')
        tree.heading('Description', text='Description')

        tree.grid(row=0, column=0, padx=20, pady=20)

        tree.column(1, width=500)
        for r in rows:
            tree.insert("", tk.END, values=(r[1], r[2]))


