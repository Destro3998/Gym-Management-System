from tkinter.constants import CENTER, END

# from PIL import ImageTk, Image
import tkinter as tk
from tkinter import Text, Tk
from tkinter.messagebox import showinfo
from Database.feed_back_db import FeedbackDB


# Gui logic
class Feedback(tk.Frame):
    feedbackString = None
    title = None

    def __init__(self, root):
        db = FeedbackDB()
        db.create_tables()
        super().__init__()
        root.title("Feedback")
        root.geometry("600x400")

        self.title = tk.Entry(self, width=40)
        self.title.focus_set()
        top_heading = tk.Label(self, text="Add Feedback", fg="black", font=("times new roman", int(20.0)), )
        top_heading.grid(row=0, column=1, columnspan=2)
        self.title.grid(row=1, column=1)
        self.feedbackString = tk.Text(self, width=40, height=5)
        self.feedbackString.grid(row=2, column=1)
        p_title = tk.Label(self, text="name")
        p_title.grid(row=1, column=0, pady=10)
        create = tk.Button(self, text="Add", command=self.create,)
        back = tk.Button(self, text="Back", command=root.go_main_nav)

        create.grid(row=6, column=1, pady=15)
        back.grid(row=7, column=1, padx=5, pady=15)

    def create(self):
        feedback_string = self.feedbackString.get("1.0", END)
        title_string = self.title.get()
        print(f".................value...............{title_string}")
        if not feedback_string:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter feedback.")
            return
        if not title_string:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter Title.")
            return
        else:
            d = FeedbackDB()
            d.add_feedback(feedback_string, title_string)
            showinfo("Added", "Successfully Added Feedback")
