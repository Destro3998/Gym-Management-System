# Damon Dix

import tkinter as tk

"""
Main Nav page, this is where the main page with the navigation button to do different tasks will be
different key users will have different functionality (admin, customers)
"""

# Imports for different page navigation's
from MemberManagement.MemberManagementUI import MemberManagementUI
from GymBookings.GymBookingsUI import GymBookingsUI
from MemberManagement.SearchMember import SearchMember


class MainNav(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Main Menu")

        # new member button to navigate to the page to add a new member
        new_member = tk.Button(self, text="New Member", command=lambda: root.change_page(MemberManagementUI))
        new_member.grid(row=0, column=0, padx=20, pady=10)

        # gym bookings button to navigate to the page to add a new member
        new_booking = tk.Button(self, text="Class Sign Up", command=lambda: root.change_page(GymBookingsUI))
        new_booking.grid(row=1, column=0, padx=20, pady=10)

        # Button to bring up member info to potentially edit or just lookup
        search_member = tk.Button(self, text="Search Member", command=lambda: root.change_page(SearchMember))
        search_member.grid(row=2, column=0, padx=20, pady=10)
