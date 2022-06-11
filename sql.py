import sqlite3


class DbCon:
    def __init__(self, db):
        # stores the db_value used for selecting the correct database
        self.db = db

    def connection_simple(self, query):
        # does not yield result, used for adding tables and other simple things
        connect = sqlite3.connect(self.db)
        connect.cursor().execute(query)
        connect.commit()
        connect.close()

    def insert(self, query, input_tuple):
        connect = sqlite3.connect(self.db)
        connect.cursor().execute(query, input_tuple)
        connect.commit()
        connect.close()

    def unpack_first_result(self, query):
        # unpacks the first item since fetch_all returns a tuple within a list/tuple
        connect = sqlite3.connect(self.db)
        result_packed = connect.cursor().execute(query).fetchall()
        result = []
        for row in result_packed:
            result.append(row[0])
        connect.close()
        return result

    def return_result(self, query):
        connect = sqlite3.connect(self.db)
        result = connect.cursor().execute(query).fetchall()
        connect.close()
        return result

    def find_user(self, name):
        # a log-in function will replace this one
        conn = sqlite3.connect(self.db)
        query = f'SELECT * FROM USER_TABLE WHERE NAME Like "{name}"'
        user = conn.cursor().execute(query).fetchone()
        conn.close()
        # Return user list
        return user

    # since building does not have its own file, can replace with connection simple function
    def add_building(self, building):
        connection = sqlite3.connect(self.db)
        connection.cursor().execute(f'INSERT INTO BUILDINGS (Building) VALUES("{building}")')
        connection.commit()
        connection.close()
