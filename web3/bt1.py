from pymongo import MongoClient
import matplotlib.pyplot as plt


mongo_uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client=MongoClient(mongo_uri)
db=client.c4e
reff = db.customers.find()
so_luong_khach=0

events=0
wom=0
ads=0
for i in reff:
    print(i["ref"])
    so_luong_khach=so_luong_khach+1
    if i["ref"]=="events":
        events=events+1
    if i["ref"]=="ads":
        ads=ads+1
    if i["ref"]=="wom":
        wom=wom+1
print("số lượng khách là: ",so_luong_khach)
print("số events :",events)
print("số wom :", wom)
print("số ads :",ads)
labels = 'events', 'wom', 'ads'
sizes = [events, wom, ads]
explode = (0, 0.1, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()