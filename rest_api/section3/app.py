from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

stores = [
    {"name": "My wonderful store", "items": [{"name": "My item", "price": 19.99}]}
]


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/store", methods=["POST"])  # homepage of the site
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store)


@app.route("/store/<string:name>")
def get_store(name):

    for i in stores:
        if i["name"] == name:
            return jsonify(i)
    return jsonify({"message": "Store not found"})


@app.route("/store/")
def get_stores():
    return jsonify({"stores": stores})


@app.route("/store/<string:name>/item", methods=["POST"])  # homepage of the site
def createItemInStore(name):
    request_data = request.get_json()
    for i in stores:
        if i["name"] == name:
            i["items"].append(
                {"name": request_data["name"], "pricing": request_data["pricing"]}
            )
            return jsonify({"items": i["items"]})
    return jsonify({"message": "Store not found"})


@app.route("/store/<string:name>/item")  # homepage of the site
def getItemsInStore(name):
    for i in stores:
        if i["name"] == name:
            return jsonify({"items": i["items"]})
    return jsonify({"message": "Store not found"})


app.run(port=5000)
