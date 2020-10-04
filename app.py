from flask import Flask
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

mongo_obj = MongoClient(
    "mongodb+srv://GreenDeck:greendeck123@cluster0.0wnzx.gcp.mongodb.net/GreenDeck?retryWrites=true&w=majority")
db = mongo_obj["greendeck"]
collection = db["data"]

appobj = Flask(__name__)


@appobj.route("/")
def get_data():
    return "hello api"


@appobj.route("/database", methods=["GET"])
def data():
    dbs = list(collection.find({}))
    return json.dumps(dbs, default=json_util.default)


if __name__ == '__main__':
    appobj.run(debug=True)
