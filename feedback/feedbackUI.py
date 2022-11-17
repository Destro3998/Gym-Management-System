import tkinter as tk
import re
from tkinter.messagebox import showinfo
from feedbackDb import Feedback


"""
Class for the creation of members, members get added to a database
"""


class Window(tk.Frame):

    fullname = None
    email = None
    number = None
    message = None
    subject = None
    experience = None
    check_var1 = None
    check_var2 = None

    feed_back = Feedback()

    name_regex = re.compile('[^a-zA-Z]+')
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    message_regex = re.compile('[^0-9a-zA-z ]+')
    number_regex = re.compile('[^0-9]+')
    subject_regex = re.compile('[^0-9a-zA-z ]+')

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.geometry('600x500')

        root.eval('tk::PlaceWindow . center')
        root.title("FeedBack Page")

        # Entry forms for a basic member object creation

        promptL = tk.Label(root, text="How was your overall experience", font=("Arial", 25, "bold") )
        promptL.grid(row=3, column=3, columnspan=3)

        self.check_var1 = tk.IntVar()
        check1 = tk.Checkbutton(root, text='Good', variable=self.check_var1, onvalue=1, offvalue=0,
                                command=self.display_input)
        self.check_var2 = tk.IntVar()
        check2 = tk.Checkbutton(root, text='Bad', variable=self.check_var1, onvalue=3, offvalue=0,
                                command=self.display_input)

        check1.grid(row=5, column=2, columnspan=2)
        check2.grid(row=5, column=3, columnspan=2)

        self.fullname = tk.Entry(root, width=40)
        l_fullname = tk.Label(root, text="Full Name", font=("Arial", 15, "bold"))

        self.email = tk.Entry(root, width=40)
        l_email = tk.Label(root, text="Email", font=("Arial", 15, "bold"))

        self.number = tk.Entry(root, width=40)
        l_number = tk.Label(root, text="Phone number", font=("Arial", 15, "bold"))

        self.subject = tk.Entry(root, width=40)
        l_subject = tk.Label(root, text="Subject", font=("Arial", 15, "bold"))

        # self.message = tk.Entry(root, width=40)
        l_mess = tk.Label(root, text="Message", font=("Arial", 15, "bold"))
        self.message = tk.Text(root, width=52, height=5)

        title = tk.Label(root, text="FEEDBACK", font=("Arial", 60, "bold"), anchor="center")

        title.grid(row=0, column=3, columnspan=3, pady=30)
        l_fullname.grid(row=7, column=2, pady=10)
        l_number.grid(row=9, column=2, pady=10)
        l_subject.grid(row=10, column=2, pady=10)
        l_email.grid(row=8, column=2, pady=10)
        l_mess.grid(row=11, column=2, pady=10)

        self.fullname.grid(row=7, column=3, padx=5)
        self.email.grid(row=8, column=3, padx=5)
        self.number.grid(row=9, column=3, padx=5)
        self.subject.grid(row=10, column=3, padx=5)
        self.message.grid(row=11, column=3, padx=5)

        submit = tk.Button(root, text="Submit", command=self.save, relief="raised")
        submit.grid(row=15, column=3, columnspan=2, pady=5)

    def display_input(self):
        print("Input for check1:", self.check_var1.get())
        print("Input for check2", self.check_var2.get())

    def validate_fullname(self):
        if len(self.fullname.get()) > 50:
            return False
        else:
            return True

    def validate_email(self):
        if not self.email_regex.search(self.email.get()):
            return False
        else:
            return True

    def validate_number(self):
        if self.number_regex.search(self.number.get()):
            return False
        else:
            return True

    def validate_subject(self):
        if self.subject_regex.search(self.subject.get()):
            return False
        else:
            return True

    def save(self):
        if self.check_var1:
            self.experience = "Good"
        else:
            self.experience = "Bad"

        if [x for x in (self.fullname, self.email, self.number, self.subject, self.message) if x is None]:
            showinfo("Missing Items", "Error \nPlease make sure you fill out all required fields")
        elif not self.validate_fullname():
            showinfo("Incorrect Format", "Full name must be less than 40 characters")
        elif not self.validate_email():
            showinfo("Incorrect Format", "Not a valid email, must be in abc123@abs123.abd format")
        elif not self.validate_number():
            showinfo("Incorrect Format", "Not a valid phone number, must only contain numbers and be 10 numbers long")
        elif not self.validate_subject():
            showinfo("Incorrect Format", "Not a subject")
        else:
            Feedback.add_user(self.fullname.get(), self.email.get(), self.number.get(), self.subject.get(),
                              self.message.get("1.0", tk.END), self.experience)
            showinfo("Thank you", "Thank you for your feedback")

        self.fullname.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.number.delete(0, tk.END)
        self.subject.delete(0, tk.END)
        self.message.delete("1.0", tk.END)


if __name__ == "__main__":
    rt = tk.Tk()
    app = Window(rt)
    app.mainloop()
