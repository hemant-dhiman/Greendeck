from flask import Flask
import pymongo
import json
from bson import json_util
# importing client
from DataBaseFile.database import client
import markdown

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

count = mongo_obj["Greendeck_SE_Assignment_Task_1"]["Data"].count_documents({})

if count < 5000:
    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)
    print("database Upload done!")
else:
    print("data Already uploaded!")


@app_obj.route("/")
def get_data():
    with open(app_obj.root_path + '/README.md', 'r') as mrkdwn:
        md = mrkdwn.read()
        print(md)
    return markdown.markdown(md)
    # return 'hello api'


@app_obj.route("/database", methods=["GET"])
def data():
    dbs = list(collection.find({}))
    return json.dumps(dbs, default=json_util.default)


'''
if __name__ == '__main__':
    #app_obj.run(debug=True)
'''
