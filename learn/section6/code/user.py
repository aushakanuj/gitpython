import sqlite3
from flask_restful import Resource, reqparse


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


class UserRegister(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument(
        "username", type=str, required=True, help="Thies field cannot be blank."
    )

    parser.add_argument(
        "password", type=str, required=True, help="Thies field cannot be blank."
    )

    def post(self):

        data = UserRegister.parser.parse_args()

        if User.findByUsername(data["username"]) is None:

            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()

            inser_query = "INSERT INTO users VALUES(NULL,?,?)"

            cursor.execute(inser_query, (data["username"], data["password"]))

            connection.commit()
            connection.close()

            return {"message": "User created successfully"}, 201
        else:
            return {"message": "Username already exists,create a unique username"}, 400


#         (1, 'jose', '1102')
# (2, 'bob', '1234')
# (3, 'rol', 'qweasdzxc')
