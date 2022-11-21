# Damon Dix
# from PIL import Image, ImageTk
import tkinter as tk

"""
Main Nav page, this is where the main page with the navigation button to do different tasks will be
different key users will have different functionality (admin, customers)
"""

# Imports for different page navigation's
from MemberManagement.MemberManagementUI import MemberManagementUI
from GymBookings.GymBookingsUI import GymBookingsUI
from MemberManagement.SearchMember import SearchMember
from member_plan import MemberPlan
from plan import Plan
from trainer import Trainer
from  time_change import UpdateTime
from amenities import  Amenities
from feed_back import  Feedback
from  booking import  Booking
from  time_slots import  TimeSlots
from create_equipment import Equipments
from equipment import show_equiments
from edit_member import edit_member
from GymBookings.DeleteGYMClass import DeleteClass
from GymReporting.GymReportingUI import GymReportingUI
from GymReporting.MembershipUI import MembershipUI


class MainNav(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Main Menu")
        root.geometry("800x400")

        # # new member button to navigate to the page to add a new member
        new_member = tk.Button(self, text="New Member", command=lambda: root.change_page(MemberManagementUI), width=20)
        new_member.grid(row=1, column=0, padx=20, pady=10)

        # # gym bookings button to navigate to the page to add a new member
        new_booking = tk.Button(self, text="Sign Up/Withdraw", command=lambda: root.change_page(GymBookingsUI), width=20)
        new_booking.grid(row=1, column=1, padx=20, pady=0)

        # Button to bring up member info to potentially edit or just lookup
        search_member = tk.Button(self, text="Search Member", command=lambda: root.change_page(SearchMember), width=20)
        search_member.grid(row=1, column=2, padx=20, pady=10)

        # Button to bring up member info to potentially edit or just lookup
        plan = tk.Button(self, text="Create Plans", command=lambda: root.change_page(Plan), width=20)
        plan.grid(row=2, column=0, padx=20, pady=10)
        memebrs_plan = tk.Button(self, text="Members Plan", command=lambda: root.change_page(MemberPlan), width=20)
        memebrs_plan.grid(row=2, column=1, padx=20, pady=10)
        trainer = tk.Button(self, text="Create Trainer", command=lambda: root.change_page(Trainer), width=20)
        trainer.grid(row=2, column=2, padx=20, pady=10)

        change_time = tk.Button(self, text="Update Gym Time", command=lambda: root.change_page(UpdateTime), width=20)
        change_time.grid(row=3, column=0, padx=20, pady=10)

        amenities = tk.Button(self, text="Add Amenities", command=lambda: root.change_page(Amenities), width=20)
        amenities.grid(row=3, column=1, padx=20, pady=10)
        feedback = tk.Button(self, text="Add Feedback", command=lambda: root.change_page(Feedback), width=20)
        feedback.grid(row=3, column=2, padx=20, pady=10)
        booking = tk.Button(self, text="Add Booking", command=lambda: root.change_page(Booking), width=20)
        booking.grid(row=4, column=0, padx=20, pady=10)

        time_slots = tk.Button(self, text="Add Class", command=lambda: root.change_page(TimeSlots), width=20)
        time_slots.grid(row=4, column=1, padx=20, pady=10)

        create_equipment = tk.Button(self, text="Create Equipments", command=lambda: root.change_page(Equipments), width=20)
        create_equipment.grid(row=4, column=2, padx=20, pady=10)

        view_equipments = tk.Button(self, text="View Equipments", command=lambda: root.change_page(show_equiments), width=20)
        view_equipments.grid(row=5, column=1, padx=20, pady=10)

        update = tk.Button(self, text="Update Member Information", command=lambda: root.change_page(edit_member))
        update.grid(row=5, column=0, padx=20, pady=10)

        update = tk.Button(self, text="Delete Class", command=lambda: root.change_page(DeleteClass), width=20)
        update.grid(row=5, column=2, padx=20, pady=10)

        view_plans = tk.Button(self, text="View Plans", command=lambda: root.change_page(MembershipUI),
                               width=20)
        view_plans.grid(row=6, column=1, padx=20, pady=10)

        about_us = tk.Button(self, text="About Us", command=lambda: root.change_page(GymReportingUI),
                                    width=20)
        about_us.grid(row=6, column=0, padx=20, pady=10)

