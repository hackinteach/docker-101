from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.results import InsertOneResult
from os import getenv
import json
from bson.json_util import default

app = Flask(__name__)

_mongo_host = getenv("MONGO_HOST", "localhost")
_mongo_port = int(getenv("MONGO_PORT", 27017))

_mongo = MongoClient(_mongo_host, _mongo_port)
_db = _mongo.get_database("my_db")
_collection = _db.get_collection("simple_collection")


@app.route("/add", methods=["POST"])
def add():
    data = dict(request.json)
    res: InsertOneResult = _collection.insert_one(data)
    return jsonify({"id": str(res.inserted_id)})

@app.route("/all", methods=["GET"])
def get_all():
    found = _collection.find()
    ret = [json.loads(json.dumps(f, default=default)) for f in found]
    return jsonify(ret)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
