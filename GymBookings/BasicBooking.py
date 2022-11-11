# Ariana Fayth Quiambao


"""
This will be a basic class to create Class booking objects to be added to sqlite dtb later
Class booking object require a memberID, class name, and class time.
The class also contains basic getter and setter functions to edit the object data
"""

bookings = []

class BasicBooking:

    def __init__(self, classID, class_name, class_timeslot):
        self.classID = classID
        self.class_name = class_name
        self.class_timeslot = class_timeslot
