import sqlite3 as sq


def add_user(database, user):
    query = "INSERT INTO user (first_name, last_name, age, address, phone_number, " \
            "username, password, memberId) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"

    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute(query, user)
    connection.commit()
    connection.close()


def get_name(database, memberId):
    query = "SELECT first_name FROM user WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    cursor.execute(query, [memberId])
    rows = cursor.fetchall()
    connection.close()

    return  rows[0][0]


# update by memberId
def change_firstname(database, new_name, memberId):
    is_string = True
    query = "UPDATE user set first_name = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    try:
        int(new_name)
    except ValueError:
        is_string = False
    if is_string:
        print("Error: Invalid Datatype")
    else:
        cursor.execute(query, (new_name, memberId))
        connection.commit()
        connection.close()


def change_address(database, address, memberId):
    is_string = True
    query = "UPDATE user set address = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()
    try:
        int(address)
    except ValueError:
        is_string = False
    if is_string:
        print("Error: Invalid Datatype")
    else:
        cursor.execute(query, (address, memberId))
        connection.commit()
        connection.close()

def change_phonenumber(database, number,  memberId):
    query = "UPDATE user set phone_number = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    if isinstance(number, int):
        cursor.execute(query, (number, memberId))
        connection.commit()
        connection.close()
    else:
        print("Error: Invalid Datatype")


def change_age(database, age, memberId):
    query = "UPDATE user set age = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    if isinstance(age, int):
        cursor.execute(query, (age, memberId))
        connection.commit()
        connection.close()
    else:
        print("Error: Invalid Datatype")

def change_lastname(database, lastname, memberId):
    query = "UPDATE user set last_name = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    if isinstance(lastname, str):
        cursor.execute(query, (lastname, memberId))
        connection.commit()
        connection.close()
    else:
        print("Error: Invalid Datatype")


def change_username(database, username, memberId):
    query = "UPDATE user set username = ? WHERE memberId = ?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    if isinstance(username, str):
        cursor.execute(query, (username, memberId))
        connection.commit()
        connection.close()
    else:
        print("Error: Invalid Datatype")


def get_user_information(database, memberId):

    """
    gets a specific user information
    :param database: user database for gym system
    :param memberId: integer member id
    :return: the user information
    """
    query = "SELECT * FROM user WHERE memberId=?"
    connection = sq.connect(database)
    cursor = connection.cursor()

    cursor.execute(query, [memberId])
    rows = cursor.fetchall()

    for r in rows:
        print(r)

    connection.close()

def get_information(database):

    """    gets all user information from the database
    :param database: user database for gym system
    :param memberId: integer member id
    :return: a list of all the user information
    """

    query = "SELECT * FROM user"
    connection = sq.connect(database)
    cursor = connection.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    result = rows

    connection.close()

    return result


if __name__ == "__main__":

    r = get_information('Database/database.db')