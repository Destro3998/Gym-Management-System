# Damon Dix

import tkinter as tk

"""
Class is used to search through the 
"""


class SearchMember(tk.Frame):
    first_name = ""
    last_name = ""
    email = ""
    phone_number = ""
    address = ""

    # placeholder boolean to check whether text entry have been selected once or not
    # upon first selection, default text is deleted, and you're able to enter
    # your own text, do it this way so it won't re-delete your entry
    fn_selected = False
    ln_selected = False
    email_selected = False
    pn_selected = False
    address_selected = False

    # for the returned search spec of members
    listbox = None

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        root.title("Search Member")

        heading = tk.Label(self, text="Member Inquiry")
        heading.grid(row=0, rowspan=2, column=0, columnspan=4, pady=20, padx=40, sticky="we")

        self.listbox = tk.Listbox(self, width=67)


        # Entry fields
        self.first_name = tk.Entry(self)
        self.first_name.insert(0, "First Name...")
        self.first_name.bind("<FocusIn>", self.delete_fn_entry)

        self.last_name = tk.Entry(self)
        self.last_name.insert(0, "Last Name...")
        self.last_name.bind("<FocusIn>", self.delete_ln_entry)

        self.phone_number = tk.Entry(self)
        self.phone_number.insert(0, "Phone Number...")
        self.phone_number.bind("<FocusIn>", self.delete_num_entry)

        self.email = tk.Entry(self)
        self.email.insert(0, "Email...")
        self.email.bind("<FocusIn>", self.delete_email_entry)

        self.address = tk.Entry(self)
        self.address.insert(0, "Address...")
        self.address.bind("<FocusIn>", self.delete_addy_entry)

        back = tk.Button(self, text="Back", command=root.go_main_nav)
        clear = tk.Button(self, text="Reset", width=5, command=self.clear_searches)
        search = tk.Button(self, text="Search", width=5, command=self.search_member)
        edit = tk.Button(self, text="Edit", width=5, command=self.edit_member)
        delete = tk.Button(self, text="Delete", width=5, command=self.delete_selected_member)



        # The grid layout
        self.first_name.grid(row=3, column=0, padx=5, pady=5)
        self.last_name.grid(row=3, column=1, padx=5, pady=5)
        self.phone_number.grid(row=3, column=2, padx=5,pady=5)
        self.email.grid(row=4, column=0, padx=5, pady=5)
        self.address.grid(row=4, column=1, padx=5,pady=5)
        search.grid(row=3, column=3, padx=5, sticky="w")
        clear.grid(row=4, column=3, padx=5, sticky="w")
        edit.grid(row=13, column=3, padx=5, sticky="sw")
        delete.grid(row=14, column=3, padx=5, sticky="sw")
        back.grid(row=15, column=0, pady=10, padx=10, sticky="w")
        self.listbox.grid(row=5, column=0, columnspan=4, rowspan=10, padx=5, sticky="w")

    def search_member(self):
        pass

    def edit_member(self):
        pass

    def delete_selected_member(self):
        pass

    # Just for effects, deletes text in entry form if selected (the first time or after clear)
    def delete_fn_entry(self, event):
        if not self.fn_selected:
            self.fn_selected = True
            self.first_name.delete(0, 'end')

    def delete_ln_entry(self, event):
        if not self.ln_selected:
            self.ln_selected = True
            self.last_name.delete(0, 'end')

    def delete_email_entry(self, event):
        if not self.email_selected:
            self.email_selected = True
            self.email.delete(0, 'end')

    def delete_num_entry(self, event):
        if not self.pn_selected:
            self.pn_selected = True
            self.phone_number.delete(0, 'end')

    def delete_addy_entry(self, event):
        if not self.address_selected:
            self.address_selected = True
            self.address.delete(0, 'end')

    # Reset search and selection variables so they dissappear when you click on them again
    def clear_searches(self):
        self.first_name.delete(0, 'end')
        self.first_name.insert(0,"First Name...")
        self.fn_selected = False
        self.last_name.delete(0, 'end')
        self.last_name.insert(0, "Last Name...")
        self.ln_selected = False
        self.email.delete(0, 'end')
        self.email.insert(0, "Email...")
        self.email_selected = False
        self.phone_number.delete(0, 'end')
        self.phone_number.insert(0, "Phone Number...")
        self.pn_selected = False
        self.address.delete(0, 'end')
        self.address.insert(0, "Address...")
        self.address_selected = False
        self.listbox.delete(0, 'end')
