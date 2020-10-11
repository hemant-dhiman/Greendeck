import threading
import webbrowser
import pymongo
from pymongo import MongoClient
from flask import Flask, request
import json
from bson import json_util
import markdown

# importing client
from DataBaseFile.database import client

mongo_obj = client()

db = mongo_obj["Greendeck_SE_Assignment_Task_1"]
collection = db["Data"]

'''
db = mongo_obj["greendeck"]
collection = db["data"]
'''

app_obj = Flask(__name__)

# open the data base file in locally
with open("DataBaseFile/Greendeck SE Assignment Task 1.json") as file:
    file_data = json.load(file)

# give _id to every entry
for i in range(0, 5000):
    file_data[i]['_id'] = i

# count the total entries
count = collection.count_documents({})

if count < 5000:
    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)
    print("database Upload done!")
else:
    print("data Already uploaded!")


# Homepage
@app_obj.route("/")
def get_data():
    with open(app_obj.root_path + '/README.md', 'r') as mrkdwn:
        md = mrkdwn.read()
        return markdown.markdown(md)
    # return 'hello api'


# view database
@app_obj.route("/database", methods=["GET"])  # get all the data from the collection
def data():
    dbs = list(collection.find({}))
    return json.dumps(dbs, default=json_util.default)


# view single entry
@app_obj.route("/database/id/<int:i_d>/", methods=["GET"])  # get one data in the collection
def one_data(i_d):
    dbs = collection.find_one(
        {"_id": int(i_d)}
    )
    if dbs is not None:
        return str(dbs)
    else:
        return {"Message": "Not Found"}, 404


@app_obj.route("/newdata", methods=["POST"])
def new():
    new_data = request.json
    # count the latest id
    ids = collection.count_documents({})

    d = collection.find_one(
        {"_id": int(new_data["_id"])}
    )
    if d is None:
        new_data["_id"] = ids + 1  # give new_entry _id attribute a unique value
        collection.insert_one(new_data)
        return {"Inserted": str(new_data)}, 201
    else:
        return {"Message": "Id Already exist " + str(d)}

# update

# delete
