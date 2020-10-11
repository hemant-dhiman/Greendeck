from pymongo import MongoClient
from flask import request, Flask, jsonify

mongo_obj = MongoClient(
    "mongodb+srv://GreenDeck:greendeck123@cluster0.0wnzx.gcp.mongodb.net/GreenDeck?retryWrites=true&w=majority")

# db = mongo_obj["Greendeck_SE_Assignment_Task_1"]
# collection = db["Data"]
''' single row
d = collection.find_one(
    {"_id": 500}
)

print(len(list(d)))
print(d)
for k in d:
    print(k, ":", d[k])
'''

'''insert new value'''
db = mongo_obj["greendeck"]
collection = db["data"]

app = Flask(__name__)


@app.route("/")
def data():
    _data = collection.find({})
    return jsonify(_data)


@app.route("/entry", methods=["POST"])
def new_entry():
    request_data = request.json
    d = collection.find_one(
        {"_id": int(request_data["_id"])}
    )
    if d is None:
        collection.insert_one(request_data)
        return {"Inserted": str(request_data)}, 200
    else:
        return {"Message": "Id Already exist " + str(d)}



'''
    # check the existing id
    ids = int(collection.count_documents({}))
    _data = {
        "_id": ids + 1,
        "name": str(request_data["name"]),
        "brand_name": str(request_data["brand_name"]),
        "regular_price_value": int(request_data["regular_price_value"]),
        "offer_price_value": int(request_data["offer_price_value"]),
        "currency": str(request_data["currency"]),
        "classification_l1": str(request_data["classification_l1"]),
        "classification_l2": str(request_data["classification_l2"]),
        "classification_l3": str(request_data["classification_l3"]),
        "classification_l4": str(request_data["classification_l4"]),
        "image_url": str(request_data["image_url"])
    }
'''

# obj = Flask(__name__)

'''
obj = Flask(__name__)
obj.secret_key = "secretkey"
obj.config['MONGO_URI'] = "mongodb+srv://temp_data:123456Hd@cluster0.rz38v.mongodb.net/temp_data?retryWrites=true&w=majority"
mongo = PyMongo(obj)


if __name__ == '__main__':
    print("Application started!")
    obj.run(debug=True)
'''
