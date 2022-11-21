
"""
This will serve as the main container for all of the UI's/Different pages

"""
import tkinter as tk
from login import LoginPage
from MainNav import MainNav
from UserAdmin import User, Admin
from create_equipment import Equipments

class MainUI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.page = None
        tk.Tk.resizable(self, width=True, height=True)
        window_height = 800
        window_width = 900

        screen_width = tk.Tk.winfo_screenwidth(self)
        screen_height = tk.Tk.winfo_screenheight(self)
        x_cordinate = int((screen_width / 2) - (window_width / 2))-50
        y_cordinate = int((screen_height / 2) - (window_height / 2))-50

        tk.Tk.geometry(self, "{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.change_page(LoginPage)  # The initial page will be the login page upon startup

    def change_page(self, newPage):
        # create instance for new page to be added to main root
        cur_page = newPage(self)

        # get rid of the old page, if there is one showing, otherwise pass
        if self.page is not None:
            self.page.destroy()

        # set new page and pack it into root container
        self.page = cur_page
        self.page.pack()
        self.eval('tk::PlaceWindow . center')

    def go_main_nav(self):
        if self.page is not None:
            self.page.destroy()
        self.page = User(self)
        self.page.pack()

    def go_main_nav1(self):
        if self.page is not None:
            self.page.destroy()
        self.page = Admin(self)
        self.page.pack()


if __name__ == "__main__":
    gui = MainUI()
    gui.mainloop()
