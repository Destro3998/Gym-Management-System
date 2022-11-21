import dbconnection as con
import json as j
import sqlite3 as sq


def get_user_information(conn, memberID):
    """

    :param conn:
    :param memberID:
    :return:
    """

    conn.row_factory = con.sq.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE memberID=?", (memberID,))

    try:
        row = dict(cur.fetchone())
        return row
    except TypeError:
        return False
