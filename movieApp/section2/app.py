from flask import Flask, request
import requests
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.secret_key = "1234"
api = Api(app)

jwt = JWT(app, authenticate, identity)

movies = [{"name": "Avengers", "type": "action"}]


class Movie(Resource):
    @jwt_required()
    def get(self, name):
        x = Movie.getMovies(name)
        return {"movies": x}, 200 if x else 500

    @classmethod
    def getMovies(clc, name):
        try:
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
        except:
            return None

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, movies), None):
            return {"Movie with the name {} already exists".format(name)}, 400
        request_data = request.json()
        movies.append({"name": name, "type": request_data})
        return {"my movies": movies}, 200

    def update(self, name):
        if next(filter(lambda x: x["name"] == name, movies), None):
            request_data = request.json()
            movies[name] = request_data
            return {"name": name, "type": request_data}, 200

    def delete(self, name):
        if next(filter(lambda x: x.name == name, movies), None):
            return {"message": ("the movie {} does not exist".format(name))}, 400
        for i, movie in enumerate(movies):
            if movie.name == name:
                movies.pop(i)
                break
        return {"message": "The movie has been deleted"}, 200


class Movies(Resource):
    def getAllMovies(self):
        return {"movies": movies}, 200


api.add_resource(Movie, "/movie/<string:name>")
api.add_resource(Movies, "/movies")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
