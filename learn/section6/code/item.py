from flask_restful import Resource, reqparse

from flask_jwt import jwt_required
import sqlite3

items = []


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank"
    )

    @jwt_required()
    def get(self, name):
        try:
            result = Item.findByname(name)
        except:
            return {"message": "Error retrieving the data"}, 500
        if result:
            return result
        return {"message": "Item does not exist"}, 400

    @classmethod
    def findByname(clc, name):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        result = result.fetchone()
        connection.close()
        if result:
            return {"name": result[0], "price": result[1]}, 200

    @classmethod
    def writeItem(clc, name, request_data):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        insert_query = "INSERT INTO items VALUES(?,?)"
        cursor.execute(insert_query, (name, request_data["price"]))
        connection.commit()
        connection.close()

    @classmethod
    def updateItem(clc, name, request_data):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        update_query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(update_query, (request_data["price"], name))
        connection.commit()
        connection.close()

    def post(self, name):
        result = Item.findByname(name)
        if result:
            return {"message": "item already exists"}, 400
        request_data = Item.parser.parse_args()
        try:
            Item.writeItem(name, request_data)
        except:
            return {"message": "Error occured while inserting the data"}, 500
        return {"message": "Item created"}, 201

    def put(self, name):
        try:
            item = Item.findByname(name)
        except:
            return {"message": "Error in the database"}, 500
        request_data = Item.parser.parse_args()
        if item:
            Item.updateItem(name, request_data)
            return {"message": "Item modified"}, 200
        else:
            Item.writeItem(name, request_data)
            return {"message": "item added to the list"}, 201

    def delete(self, name):
        try:
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()
            update_query = "DELETE FROM items WHERE name=?"
            cursor.execute(update_query, (name,))
            connection.commit()
            connection.close()
            return {"message": "Item deleted."}, 200
        except:
            return {"message": "Error in deleting the item"}, 500


class ItemList(Resource):
    def get(self):
        try:
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()

            select_query = "SELECT * FROM items"
            items = []
            for row in cursor.execute(select_query):

                item = {"name": row[0], "price": row[1]}
                items.append(item)
            return {"items": items}
        except:
            return {"message": "Error getting the item"}, 500

