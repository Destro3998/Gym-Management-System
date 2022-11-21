# Ariana Fayth Quiambao

import sqlite3

"""
This will be a basic class to create Class booking objects to be added to sqlite dtb later
Class booking object require a memberID, class name, and class time.
The class also contains basic getter and setter functions to edit the object data
"""

amenities = []

class BasicReporting:

    def __init__(self, amenityID, amenity_name):
        self.amenityID = amenityID
        self.amenity_name = amenity_name

    def get_amenities(self):
        connection = sqlite3.connect(r'Database.db')
        cursor = connection.execute('select * from amenities')
        for row in cursor.fetchall():
            amenities.append(BasicReporting(row[0], row[1]))
        connection.close()

staff = []

class BasicStaff:
    def __init__(self, id, staff_fname, staff_lname, staff_email, staff_phone, staff_adrress, staff_specialist):
        self.id = id
        self.staff_fname = staff_fname
        self.staff_lname = staff_lname
        self.staff_email = staff_email
        self.staff_phone = staff_phone
        self.staff_address = staff_adrress
        self.staff_specialist = staff_specialist

    def get_staff(self):
        connection = sqlite3.connect(r'Database.db')
        cursor = connection.execute('select * from trainer')
        for row in cursor.fetchall():
            staff.append(BasicStaff(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        connection.close()
