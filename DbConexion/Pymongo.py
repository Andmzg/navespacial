import pymongo

# set a 5-second connection timeout
client = pymongo.MongoClient('mongodb+srv://andmz:abc123*@cluster0.d2i3um1.mongodb.net/'
                             'estacion?retryWrites=true&w=majority', serverSelectionTimeoutMS=5000)
try:
    print(client.server_info())


except Exception:
    print("Unable to connect to the server.")


