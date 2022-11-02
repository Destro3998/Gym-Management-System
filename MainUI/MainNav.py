# Damon Dix

import tkinter as tk

"""
Main Nav page, this is where the main page with the navigation button to do different tasks will be
different key users will have different functionality (admin, customers)
"""

# Imports for different page navigation's

from MemberManagement.MemberManagementUI import MemberManagementUI


class MainNav(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Main Menu")

        # new member button to navigate to the page to add a new member
        new_member = tk.Button(self, text="New Member", command=lambda: root.change_page(MemberManagementUI))
        new_member.pack()
