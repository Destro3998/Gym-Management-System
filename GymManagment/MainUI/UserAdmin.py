import tkinter as tk
from UserAdminMenu import User, Admin

class UserAdmin(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)

        root.geometry('600x400')

        admin = tk.Button(self, text="Admin", command=lambda: root.change_page(Admin))
        admin.grid(row=4, column=0, sticky=tk.N, pady=30)

        root.title("Login Pages")
        btnSignUp = tk.Button(self, text="User", command=lambda: root.change_page(User))
        btnSignUp.grid(row=4, column=1, sticky=tk.N, pady=30)

        root.title("")
