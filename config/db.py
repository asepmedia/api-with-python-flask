import mysql.connector


class Database:
    def __init__(self):
        self.__conn = None

        if self.__conn is None:
            print("INITIALIZING DATABASE")
            self.__conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="test_next"
            )

    def connection(self):
        return self.__conn


__conn = Database()
db = __conn.connection()
