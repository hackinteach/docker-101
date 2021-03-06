from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    name = f", world; {name}"
    print(name)
    return "Hello " + name

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
