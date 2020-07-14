from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.secret_key = "12345"
api = Api(app)


jwt = JWT(app, authenticate, identity)

items = [{"name": "milk biscuits", "price": 69.99}]


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None) != None:
            return {"Message": "item with '{}' already exits".format(name)}, 400
        request_data = request.get_json()
        item = {"name": name, "price": request_data["pricing"]}
        items.append(item)
        return item, 201

    def put(self, name):
        pass

    def delete(self, name):
        pass


api.add_resource(Item, "/item/<string:name>")


class ItemList(Resource):
    def get(self):

        return {"items": items}


api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)

