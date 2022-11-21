from tkinter.constants import CENTER, END

# from PIL import ImageTk, Image
import tkinter as tk
from tkinter.messagebox import showinfo
from Database.amenities_db import AmenitiesDB


# Gui logic
class Amenities(tk.Frame):
    amenitiesString = None

    def __init__(self, root):
        db=AmenitiesDB()
        db.create_tables()
        super().__init__()
        root.title("Amenities")
        root.geometry("444x234")
        root.minsize(200, 400)
        root.maxsize(800, 400)
        top_heading = tk.Label(self, text="Create Amenities", fg="black", font=("times new roman", int(20.0)), )
        top_heading.grid(row=0, column=1, columnspan=2)
        label = tk.Label(self, text="Amenities")
        label.grid(row=1, column=1, )
        self.amenitiesString = tk.Text(self, width=40, height=5)

        self.amenitiesString.focus_set()
        self.amenitiesString.grid(row=2, column=1)
        create = tk.Button(self, text="Add", command=self.create)
        back = tk.Button(self, text="Back", command=root.go_main_nav1)

        create.grid(row=6, column=1)
        back.grid(row=7, column=1)

    def create(self):
        amenities_string = self.amenitiesString.get("1.0", END)
        print(f".................value...............{amenities_string}")
        if not amenities_string:
            tk.messagebox.showerror(
                title="Empty Fields!", message="Please enter amenities.")
            return
        else:
            d = AmenitiesDB()
            d.add_amenities(amenities_string)

            showinfo("Added", "Successfully Added Member")
