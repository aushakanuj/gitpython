import sqlite3
from flask_restful import Resource, reqparse


from models.user import UserModel


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

        if UserModel.findByUsername(data["username"]) is None:

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
