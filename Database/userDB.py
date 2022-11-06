
class firstName:

    def __init__(self):

        self.firstname = ""

    """:param name: String name to be set
        :return: None
        """
    def set_name(self, name):
        self.firstname = name

    """:return: The fullname as a string"""
    def get_name(self):
        return self.firstname


class lastName:

    def __init__(self):

        self.lastname = ""

    def set_name(self, name):
        self.lastname = name

    def get_name(self):
        return self.lastname


class preferredName:

    def __init__(self):
        self.preferredname = ""

    def set_name(self, name):
        self.preferredname = name

    def get_name(self):
        return self.preferredname


""" return the user's full name"""
class fullname:

    """ default constructor"""
    def __init__(self):
        self.first = firstName()
        self.last = lastName()
        self.preferred = preferredName()
        self.fullname = ""

    def set_firstname(self, name):
        self.first.set_name(name)

    def get_firstname(self):
        return self.first.get_name()

    def set_lastname(self, name):
        self.last.set_name(name)

    def get_lastname(self):
        return self.last.get_name()

    def set_preferredname(self, name):
        self.preferred.set_name(name)

    def get_preferredname(self):
        return self.preferred.get_name()

    def get_fullname(self):
        self.fullname = self.get_firstname() + " " + self.get_lastname()
        return self.fullname


class Address:

    def __init__(self):
        self.address = ""

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address


class Age:

    def __init__(self):
        self.age = 0

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


class Information:

    def __init__(self):
        self.Information = {}

    def set_username(self, username):
        self.Information['username'] = username

    def set_memberId(self, memberID):
        self.Information['memberID'] = memberID

    def set_email(self, email):
        self.Information['email'] = email

    def set_membershipPlan(self, plan):
        self.Information['membership plan'] = plan

    def set_age(self, age: Age):
        self.Information['age'] = age

    def set_address(self, address: Address):
        self.Information['address'] = address

    def get_username(self):
        return self.Information['username']

    def get_memberId(self):
        return self.Information['memberID']

    def get_membershipPlan(self):
        return self.Information['membership plan']

    def get_age(self):
        return self.Information['age']

    def get_address(self):
        return self.Information['address']

    def get_email(self):
        return self.Information['email']


class UserProfile:

    def __init__(self, fullName: fullname, information: Information):
        """

        :param fullName: The user's full name
        :param address: The user's address
        :param information: a list of user information
        :param age: the user's age
        """

        self.uprofile = {
            'name': fullName,
            'user_information': information,
        }

    def get_name(self):
        return self.uprofile['name']

    def get_info(self):
        return self.uprofile['user_information']
