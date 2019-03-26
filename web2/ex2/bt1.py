from pymongo import MongoClient


mongo_uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client= MongoClient(mongo_uri)
db=client.c4e
new={
    "title":"09",
    "author":"mrđat",
    "content":"anh cần em kề bên rồi t cùng nhau già đi"

}
db.posts.insert_one(new)













