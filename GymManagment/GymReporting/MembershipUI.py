import sqlite3
import tkinter as tk
from tkinter import ttk
from Database.plan_db import PlanDB


class MembershipUI(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Membership Plans")

        self.db = PlanDB()
        root.geometry("800x500")
        top_fram = tk.Frame(self)
        top_fram.pack()

        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        row = cur.execute("SELECT * FROM plans")
        rows = row.fetchall()

        columns = ('Membership Plan', 'Price', 'Duration',)
        tree = ttk.Treeview(top_fram, columns=columns, show='headings', )

        back = tk.Button(self, text="Back", command=root.go_main_nav)
        back.pack()

        # define headings
        tree.heading('Membership Plan', text='Membership Plan')
        tree.heading('Price', text='Price')
        tree.heading('Duration', text='Duration')

        tree.grid(row=0, column=0, padx=20, pady=20)

        tree.column(1, width=500)
        for r in rows:
            tree.insert("", tk.END, values=(r[1], r[2], r[4]))


