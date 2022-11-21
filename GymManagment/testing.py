import commands as cmd

user = ('Joey', 'Musk', 23, '051 Walt Street, TX', 306723453, 'joey_musk', 'joeyMusk123', 8, 'Advanced', 5)

database = 'Database.db'

# using a list untili get a database for membership plan
plan_list = [('Beginner', 1), ('Intermediate', 3), ('Advanced', 5)]
def TC01():
    print("TC01: Update user address with the right datatype")

    address = '1601 Aird Street, S7N1Z8, SK, Saskatoon'
    member_id = 4
    cmd.change_address(database, address, member_id)

    if cmd.get_address(database, member_id) != address:
        print("Error in TC01\n")
    else:
        print("TC01 Passed\n")

def TC02():
    print("TC02: Update user address with the wrong datatype")

    address = 12345
    member_id = 4
    cmd.change_address(database, address, member_id)

    if cmd.get_address(database, member_id) == "1601 Aird Street, S7N1Z8, SK, Saskatoon":
        print("TC02 Passed\n")
    else:
        print("Error  in TC02: Update should not occur\n")

def TC03():
    print("TC03: Test to view user information ")

    member_id = 6
    result = cmd.get_user_information(database, member_id)
    if result[7] == member_id:
        print("TC03 Passed\n")
    else:
        print("Error in TC03\n")

def TC04():
    print("TC04: Change membership plan to a lower plan")

    cmd.update_membership_plan(database, plan_list[0], 6)
    if cmd.get_membership_plan(database, 6) == "Beginner":
        print("TC04 Passed\n")
    else:
        print("Error in TC04\n")

def TC05():
    print("TC05: Add user to the database")
    # cmd.add_user(database, user)
    result = cmd.get_user_information(database, 8)
    if result[0] == 'Joey':
        print("TC05: Passed\n")
    else:
        print("Error in TC05\n")

def TC06():
    print("TC06: Update user name with appropriate datatype")

    name = "Kimberly"
    member_id = 2
    cmd.change_firstname(database, name, member_id)
    result = cmd.get_firstname(database, 2)
    if result == 'Kimberly':
        print("TC06: Passed\n")
    else:
        print("Error in TC06\n")

def TC07():
    print("TC07: Update user name with wrong datatype")

    name = ["Kimberly"]
    member_id = 3
    cmd.change_firstname(database, name, member_id)
    result = cmd.get_firstname(database, 3)
    if result != 'Kimberly':
        print("TC07: Passed\n")
    else:
        print("Error in TC07\n")


def TC08():
    print("TC08: Update user phone number ")

    number = 6895678902
    member_id = 4
    cmd.change_phonenumber(database, number, member_id)
    result = cmd.get_phonenumber(database, 4)
    if result == number:
        print("TC08: Passed\n")
    else:
        print("Error in TC08\n")

def TC09():
    print("TC09: Change user membership plan to higher plan")

    member_id = 1
    cmd.update_membership_plan(database, plan_list[2], member_id)
    result = cmd.get_membership_plan(database, member_id)
    if result == plan_list[2][0]:
        print("TC09: Passed\n")
    else:
        print("Error in TC09\n")


if __name__ == "__main__":

    TC01()
    TC02()
    TC03()
    TC04()
    TC05()
    TC06()
    TC07()
    TC08()
    TC09()

