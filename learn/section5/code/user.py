import sqlite3


class User:
    def __init__(self, _id, username, password):

        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findByUsername(cls, username):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def findById(cls, _id):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        connection.close()
        return user


#         (1, 'jose', '1102')
# (2, 'bob', '1234')
# (3, 'rol', 'qweasdzxc')
