import sqlite3 as sq


def add_user(database, user):
    query = "INSERT INTO USERS (first_name, last_name, age, address, phone_number\
     username, password, memberId,membership_plan, membership_plan_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO USERS (first_name, last_name, age, address, phone_number,\
    username, password, memberId,membership_plan, membership_plan_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", user)
    connection.commit()
    connection.close()


def get_firstname(database, memberId):
    query = "SELECT first_name FROM USERS WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute(query, [memberId])
    rows = cursor.fetchall()
    connection.close()

    return rows[0][0]

# update by memberId
def change_firstname(database, new_name, memberId):
    is_string = True
    query = "UPDATE USERS set first_name = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    if isinstance(new_name, str):
        cursor.execute(query, (new_name, memberId))
        connection.commit()
        connection.close()
    else:
        return "Error: Invalid Datatype"


def change_address(database, address, memberId):
    is_string = True
    query = "UPDATE USERS set address = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    try:
        int(address)
    except ValueError:
        is_string = False
    if is_string:
        return "Error: Invalid Datatype"
    else:
        cursor.execute(query, (address, memberId))
        connection.commit()
        connection.close()

def change_phonenumber(database, number,  memberId):
    query = "UPDATE USERS set phone_number = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    if isinstance(number, int):
        cursor.execute(query, (number, memberId))
        connection.commit()
        connection.close()
    else:
        return "Error: Invalid Datatype"


def change_age(database, age, memberId):
    query = "UPDATE USERS set age = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    if isinstance(age, int):
        cursor.execute(query, (age, memberId))
        connection.commit()
        connection.close()
    else:
        return "Error: Invalid Datatype"

def change_lastname(database, lastname, memberId):
    query = "UPDATE USERS set last_name = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    if isinstance(lastname, str):
        cursor.execute(query, (lastname, memberId))
        connection.commit()
        connection.close()
    else:
        return "Error: Invalid Datatype"


def change_username(database, username, memberId):
    query = "UPDATE USERS set username = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    if isinstance(username, str):
        cursor.execute(query, (username, memberId))
        connection.commit()
        connection.close()
    else:
        return "Error: Invalid Datatype"

def update_membership_plan(database, plan, memberId):
    query = "UPDATE USERS set membership_plan = ? WHERE memberId = ?"
    query1 = "UPDATE USERS set membership_plan_id = ? WHERE memberID = ? "
    connection = sq.connect(database)
    cursor = connection.cursor()

    if get_membership_plan_id(database, memberId) == plan[1]:
        return "Error: Cannot update to the same plan"
    else:
        cursor.execute(query, (plan[0], memberId))
        cursor.execute(query1, (plan[1], memberId))
        connection.commit()
        connection.close()


def get_user_information(database, memberId):

    """
    gets a specific user information
    :param database: user database for gym system
    :param memberId: integer member id
    :return: the user information
    """
    query = "SELECT * FROM USERS WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    cursor.execute(query, [memberId])
    rows = cursor.fetchall()

    connection.close()

    return rows[0]

def get_information(database):

    """    gets all user information from the database
    :param database: user database for gym system
    :param memberId: integer member id
    :return: a list of all the user information
    """

    query = "SELECT * FROM USERS"
    connection = sq.connect(database)
    cursor = connection.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    result = rows

    connection.close()

    return result

def get_lastname(database, memberId):
    query = "SELECT last_name FROM USERS WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute(query, [memberId])
    rows = cursor.fetchall()
    connection.close()

    return rows[0][0]


def get_address(database, memberId):
    query = "SELECT address FROM USERS WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute(query, [memberId])
    rows = cursor.fetchall()
    connection.close()

    return rows[0][0]


def get_username(database, memberId):
    query = "SELECT username FROM USERS WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute(query, [memberId])
    rows = cursor.fetchall()
    connection.close()

    return rows[0][0]


def get_phonenumber(database, memberId):
    query = "SELECT phone_number FROM USERS WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute(query, [memberId])
    rows = cursor.fetchall()
    connection.close()

    return rows[0][0]


def get_age(database, memberId):
    query = "SELECT age FROM USERS WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute(query, [memberId])
    rows = cursor.fetchall()
    connection.close()

    return rows[0][0]

def get_membership_plan(database, memberId):
    query = "SELECT membership_plan FROM USERS WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute(query, [memberId])
    rows = cursor.fetchall()
    connection.close()

    return rows[0][0]

def get_membership_plan_id(database, memberId):
    query = "SELECT membership_plan_id FROM USERS WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute(query, [memberId])
    rows = cursor.fetchall()
    connection.close()

    return rows[0][0]


if __name__ == "__main__":

    r = get_information('Database/database.db')
