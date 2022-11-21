
import sqlite3

class MemberDatabase:

    def __init__(self, name):

        conn = sqlite3.connect('database')