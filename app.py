import threading
import webbrowser
import pymongo

from flask import Flask
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
count = mongo_obj["Greendeck_SE_Assignment_Task_1"]["Data"].count_documents({})

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
@app_obj.route("/database", methods=["GET"])
def data():
    dbs = list(collection.find({}))
    return json.dumps(dbs, default=json_util.default)

# if __name__ == '__main__':
#   app_obj.run(debug=True)
#   port = 5000
#   url = "http://127.0.0.1:{0}".format(port)
#   threading.Timer(1.25, lambda: webbrowser.open(url)).start()
#   app_obj.run(debug=False)
