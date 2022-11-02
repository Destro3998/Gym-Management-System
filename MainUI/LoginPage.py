# Damon Dix

import tkinter as tk

from MainNav import MainNav

"""
Just a placeholder page if there was a login screen, button proceeds to the main navigation menu
"""


class LoginPage(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.geometry('300x300')
        root.eval('tk::PlaceWindow . center')

        user = tk.Entry(self)
        user.insert(0, "Username...")
        user.grid(row=2, column=0, sticky=tk.N)
        user.focus_set()

        password = tk.Entry(self)
        password.insert(0, "Password...")
        password.grid(row=3, column=0, sticky=tk.N)

        title = tk.Label(self, text="Runtime Error \nGym Management Software")
        title.grid(row=1, column=0, sticky=tk.N)

        button = tk.Button(self, text="Login", command=lambda: root.change_page(MainNav))
        button.grid(row=4, column=0, sticky=tk.N)

        root.title("Login Pages")
