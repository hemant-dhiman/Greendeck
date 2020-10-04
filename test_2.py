import pymongo as pm

client = pm.MongoClient("mongodb+srv://temp_data:123456Hd@cluster0.rz38v.mongodb.net/temp_data?retryWrites=true&w=majority")

db = client.sample_airbnb

all = db.listingsAndReviews.find()

print(list(all))

for i in all:
    print(i)

#database = open("DataBaseFile/Greendeck SE Assignment Task 1.json")



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
