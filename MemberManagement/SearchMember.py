# Damon Dix

import tkinter as tk

"""
Class is used to search through the 
"""


class SearchMember(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Search Member")

        heading = tk.Label(self, text="Member Inquiry")
