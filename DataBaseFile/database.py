from pymongo import MongoClient

# Making connection
mongo_obj = MongoClient(
    "mongodb+srv://GreenDeck:greendeck123@cluster0.0wnzx.gcp.mongodb.net/GreenDeck?retryWrites=true&w=majority")

'''a = mongo_obj.list_database_names()
for i in enumerate(a):
    print(i)'''

def client():
    # returning a client
    return mongo_obj
