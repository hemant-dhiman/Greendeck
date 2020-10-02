import pymongo as pm

client = pm.MongoClient("mongodb+srv://temp_data:123456Hd@cluster0.rz38v.mongodb.net/temp_data?retryWrites=true&w=majority")

db = client.sample_airbnb

all = db.listingsAndReviews.find()

for i in all:
    print(i)