from flask_restful import Resource, reqparse
from models.item import ItemModel
from flask_jwt import jwt_required, current_identity
import sqlite3

items = []


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank"
    )

    @jwt_required()
    def get(self, name):
        print(current_identity)
        try:
            result = ItemModel.findByname(name)
        except:
            return {"message": "Error retrieving the data"}, 500
        if result:
            return result
        return {"message": "Item does not exist"}, 400

    def post(self, name):
        result = ItemModel.findByname(name)
        if result:
            return {"message": "item already exists"}, 400
        request_data = Item.parser.parse_args()
        a = ItemModel(name, request_data["price"])
        try:
            a.writeItem()
        except:
            return {"message": "Error occured while inserting the data"}, 500
        return {"message": "Item created"}, 201

    def put(self, name):
        try:
            item = ItemModel.findByname(name)
        except:
            return {"message": "Error in the database"}, 500
        request_data = Item.parser.parse_args()
        a = ItemModel(name, request_data["price"])
        if item:
            a.updateItem()
            return {"message": "Item modified"}, 200
        else:
            a.writeItem()
            return {"message": "item added to the list"}, 201

    def delete(self, name):
        try:
            item = ItemModel.findByname(name)
            if item:
                pass
            else:
                return {"message": "item not found"}, 400
        except:
            return {"message": "Error in deleting the item"}, 500
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
