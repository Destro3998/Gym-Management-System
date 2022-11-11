# Ariana Fayth Quiambao


"""
This will be a basic class to create Class booking objects to be added to sqlite dtb later
Class booking object require a memberID, class name, and class time.
The class also contains basic getter and setter functions to edit the object data
"""


class BasicBooking:

    def __init__(self, class_name, class_timeslot, class_availability,
                 class_staffinstructor):
        self.class_name = class_name
        self.class_timeslot = class_timeslot
        self.class_availability = class_availability
        self.class_staffinstructor = class_staffinstructor

    ############# GETTER & SETTERS ##############################################
    # fix later to use Models.Class

    def get_class_name(self):
        return self.class_name

    def get_class_timeslot(self):
        return self.class_timeslot

    def class_availability(self):
        return self.class_availability

    def class_staffinstructor(self):
        return self.class_staffinstructor


    def set_class_name(self, class_name):
        self.class_name = class_name

    def set_class_timeslot(self, class_timeslot):
        self.classTime = class_timeslot

    def set_class_availability(self, class_availability):
        self.class_availability = class_availability

    def set_class_staffinstructor(self, class_staffinstructor):
        self.class_staffinstructor = class_staffinstructor
