# Damon Dix

"""
This will serve as the main container for all of the UI's/Different pages

"""
import tkinter as tk
from LoginPage import LoginPage


class MainUI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.page = None
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
        # self.title = title


if __name__ == "__main__":
    gui = MainUI()
    gui.mainloop()
