from flask import Flask,jsonify

app = Flask(__name__)

frameworks = [
    {
        "id":1,
        "name":"Flask"
    },

    {
        "id":2,
        "name":"Express"

    }
]


@app.route('/')
def index():
    return 'Hello World'


@app.route("/api/frameworks/",methods=["GET"])
def get_frameworks():
    return jsonify(frameworks)


if __name__ == '__main__':
    app.run(debug=True)
