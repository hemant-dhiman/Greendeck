from pymongo import MongoClient

# Making connection
mongo_obj = MongoClient(
    "mongodb+srv://GreenDeck:greendeck123@cluster0.0wnzx.gcp.mongodb.net/GreenDeck?retryWrites=true&w=majority")


def client():
    # returning a client
    return mongo_obj
