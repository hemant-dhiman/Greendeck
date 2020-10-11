from pymongo import MongoClient
import json

# Making connection
mongo_obj = MongoClient(
    "mongodb+srv://GreenDeck:greendeck123@cluster0.0wnzx.gcp.mongodb.net/GreenDeck?retryWrites=true&w=majority")

'''a = mongo_obj.list_database_names()
for i in enumerate(a):
    print(i)
'''


def client():
    # returning a client
    return mongo_obj


# db = mongo_obj["Greendeck_SE_Assignment_Task_1"]
# collection = db["Data"]

# dbs = list(collection.find({}))

# print(dbs[0])
'''
with open("Greendeck SE Assignment Task 1.json") as file:
    file_data = json.load(file)

file_data[0]['_id'] = 1

print(file_data[0]['_id'])
'''
