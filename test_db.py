import pymongo
from pprint import pprint
'''
client = pymongo.MongoClient("mongodb+srv://temp_data:123456@@cluster0.rz38v.mongodb.net/temp_data?retryWrites=true&w=majority")
'''


client = pymongo.MongoClient("mongodb+srv://temp_data:123456Hd@cluster0.rz38v.mongodb.net/temp_data?retryWrites=true&w=majority")
db = client.HD
print(db)

data = {
    "name": 'subir sardar',
    'rating': 4,
    'cuisin': 'HR'
}

re = db.KH.insert_one(data)
print("inserted {0}".format(re.inserted_id))

#data = db.sample_airbnb.listingsAndReviews.find_one({'rating': 1})
#data = db.KH.find_one({'rating': 1})
data = db.KH.find()
for i in data:
    print(i)

