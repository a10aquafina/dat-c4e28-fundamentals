from pymongo import MongoClient
mongo_uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client=MongoClient(mongo_uri)
db=client.c4e
rivers = db.river.find()
for i in rivers:
    if i["continent"]=="S. America" and i["length"]<1000:
        print("rivers in S. America< 1000km : ",i["name"])