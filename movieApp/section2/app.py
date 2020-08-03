from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


mymovies = []


class User:
    def __init__(self, _id, username, password, movies):
        self.id = _id
        self.username = username
        self.password = password
        self.movies = movies


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/movie/<string:name>")
def search(name):
    return jsonify(getMovies(name))


def getMovies(name):
    baseURL = "https://tastedive.com/api/similar"
    key = "364383-movies-XCYHUSC3"
    param = {}
    param["q"] = name
    param["k"] = key
    param["limit"] = 5
    param["type"] = "movies"
    resp = requests.get(baseURL, params=param)
    r = resp.json()
    return r["Similar"]["Results"]


@app.route("/movie/<string:name>", method=["POST"])
def addMovie(name):
    mymovies.append(name)
    return jsonify({"My movies": mymovies})


@app.route("/movies")
def getAllMovies():

    return jsonify({"My movies": mymovies})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
