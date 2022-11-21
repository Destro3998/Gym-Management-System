import tkinter as tk
from user import User
from UserAdmin import UserAdmin


class LoginPage(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)

        root.geometry('600x500')
        title = tk.Label(self, text="Welcome to THE GYM", fg="black", font=("times new roman", int(20.0)), pady=30)
        title.grid(row=1, column=1, sticky=tk.N)
        user_label = tk.Label(self, text="Enter Username", padx=10)
        user_label.grid(row=2, column=0, sticky=tk.N)
        user = tk.Entry(self)
        user.grid(row=2, column=1, sticky=tk.N)
        user.focus_set()
        user_label = tk.Label(self, text="Enter Password", pady=20, padx=10)
        user_label.grid(row=3, column=0, sticky=tk.N)
        password = tk.Entry(self, show="●")
        password.grid(row=3, column=1, sticky=tk.N, pady=20)

        root.title("Login Pages")
        btnSignUp = tk.Button(self, text="SignUp", command=lambda: root.change_page(User), width=20)
        btnSignUp.grid(row=4, column=0, sticky=tk.N, pady=30)

        btnuserA = tk.Button(self, text="Login", command=lambda: root.change_page(UserAdmin), width=20)
        btnuserA.grid(row=4, column=1, sticky=tk.N, pady=30)

        root.title("Login Pages")
