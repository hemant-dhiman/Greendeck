from flask import Flask
import pymongo
import json
from bson import json_util
from DataBaseFile.database import client

'''
mongo_obj = MongoClient(
    "mongodb+srv://GreenDeck:greendeck123@cluster0.0wnzx.gcp.mongodb.net/GreenDeck?retryWrites=true&w=majority")
'''
mongo_obj = client()
db = mongo_obj["greendeck"]
collection = db["data"]

app_obj = Flask(__name__)


@app_obj.route("/")
def get_data():
    return "hello api"


@app_obj.route("/database", methods=["GET"])
def data():
    dbs = list(collection.find({}))
    return json.dumps(dbs, default=json_util.default)


if __name__ == '__main__':
    app_obj.run(debug=True)
