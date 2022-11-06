# Ariana Fayth Quiambao

import tkinter as tk
from tkinter.messagebox import showinfo
from GymBookings.BookingsTest import test1, test2, test3

"""

"""


class GymBookingsUI(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Classes")

        # Labels for entry forms
        l_class = tk.Label(self, text="Class: ")
        l_time = tk.Label(self, text="Time: ")

        # fix later to automate l_class# = tk.Label(self, text=get_class_name)
        l_class1 = tk.Label(self, text=test1[0])
        l_class2 = tk.Label(self, text=test2[0])
        l_class3 = tk.Label(self, text=test3[0])

        # fix later to automate l_time# = tk.Label(self, text="get_class_timeslot")
        l_time1 = tk.Label(self, text=test1[1])
        l_time2 = tk.Label(self, text=test2[1])
        l_time3 = tk.Label(self, text=test3[1])

        # Title label for page
        title = tk.Label(self, text="Book A Class")

        # place everything in a grid for organization and view

        title.grid(row=0, column=0, columnspan=2, pady=30)

        l_class.grid(row=1, column=0, pady=10)
        # fix later to automate l_class#.grid(row=#, column=0, pady=10)
        l_class1.grid(row=2, column=0, pady=10)
        l_class2.grid(row=3, column=0, pady=10)
        l_class3.grid(row=4, column=0, pady=10)

        l_time.grid(row=1, column=1, padx=5)
        # fix later to automate l_time#.grid(row=#, column=1, padx=5)
        l_time1.grid(row=2, column=1, padx=5)
        l_time2.grid(row=3, column=1, padx=5)
        l_time3.grid(row=4, column=1, padx=5)

        # fix later to automate
        def popup_signup1():
            if test1[2] == "yes":
                showinfo("Unuccessful!", "Already Signed Up to Class!")
            elif test3[2] == "yes":
                showinfo("Unuccessful!", "Time Conflict!")
            else:
                test1[2] = "yes"
                showinfo("Successful!", "Signed Up to Class!")

        def popup_signup2():
            if test2[2] == "yes":
                showinfo("Unuccessful!", "Already Signed Up to Class!")
            else:
                test2[2] = "yes"
                showinfo("Successful!", "Signed Up to Class!")

        def popup_signup3():
            if test3[2] == "yes":
                showinfo("Unuccessful!", "Already Signed Up to Class!")
            elif test1[2] == "yes":
                showinfo("Unuccessful!", "Time Conflict!")
            else:
                test3[2] = "yes"
                showinfo("Successful!", "Signed Up to Class!")

        # sample automation
        """
        # loop plane(2, #), # - 2 + no. of classes
        # say, there are 3 classes
        signupplane = []
        for i in range(2,5):
            signupplane.append((2,i))

        for x, y in signupplane:
            signUp = tk.Button(self, text="Sign Up", command=popup_signup)
            signUp.grid(row=y, column=x)
        """

        # fix later to automate
        signUp1 = tk.Button(self, text="Sign Up", command=popup_signup1)
        signUp1.grid(row=2, column=2)

        signUp2 = tk.Button(self, text="Sign Up", command=popup_signup2)
        signUp2.grid(row=3, column=2)

        signUp3 = tk.Button(self, text="Sign Up", command=popup_signup3)
        signUp3.grid(row=4, column=2)

        ###################################

        def popup_withdraw1():
            if test1[2] == "no":
                showinfo("Unuccessful!", "Not Signed Up to Class!")
            else:
                test1[2] = "no"
                showinfo("Successful!", "Withdrew from Class!")

        def popup_withdraw2():
            if test2[2] == "no":
                showinfo("Unuccessful!", "Not Signed Up to Class!")
            else:
                test2[2] = "no"
                showinfo("Successful!", "Withdrew from Class!")

        def popup_withdraw3():
            if test3[2] == "no":
                showinfo("Unuccessful!", "Not Signed Up to Class!")
            else:
                test3[2] = "no"
                showinfo("Successful!", "Withdrew from Class!")

        # sample automation
        """
        def popup_withdraw():
            showinfo("Successful!", "Withdrew from Class!")
        
        withdrawplane = []
        for i in range(2,5):
            withdrawplane.append((3,i))

        for x, y in withdrawplane:
            # Button to add member to Dtb
            withdraw = tk.Button(self, text="Withdraw", command=popup_withdraw)
            withdraw.grid(row=y, column=x)
        """

        # fix later to automate
        withdraw1 = tk.Button(self, text="Withdraw", command=popup_withdraw1)
        withdraw1.grid(row=2, column=3)

        withdraw2 = tk.Button(self, text="Withdraw", command=popup_withdraw2)
        withdraw2.grid(row=3, column=3)

        withdraw3 = tk.Button(self, text="Withdraw", command=popup_withdraw3)
        withdraw3.grid(row=4, column=3)
