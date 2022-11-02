# Damon Dix


"""
This will be a basic class to create Customer member objects to be added to sqlite dtb later
Basic member object require a first name, last name, email, phone number, as well as an address
The class also contains basic getter and setter functions to edit the object data
"""


class BasicMember:

    def __init__(self, first_name, last_name, email, number, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.number = number
        self.address = address

    ############# GETTER & SETTERS ##############################################

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_number(self):
        return self.number

    def get_address(self):
        return self.address

    def set_first_name(self, name):
        self.first_name = name

    def set_last_name(self, name):
        self.last_name = name

    def set_email(self, email):
        self.email = email

    def set_number(self, number):
        self.number = number

    def set_address(self, address):
        self.address = address
