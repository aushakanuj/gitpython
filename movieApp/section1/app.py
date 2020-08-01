from flask import Flask, jsonify, request, render_template


app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/movie/<string:name>")
def search():
    pass


if __name__ == "__main__":
    app.run(port=500, debug=True)
