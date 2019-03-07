fruit={
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3,
}
strock={
    "banana":6,
    "apple":0,
    "orange":32,
    "pear":15,
}
item=["banana","apple","orange","pear"]
tong=0
for i,j in fruit.items():
    print("amount:",i,j)
for h,k in strock.items():
    print("price:",h,k)
for m in range(0,4,1):
    a=fruit[item[m]]*strock[item[m]]
# a=fruit["banana"]*strock["banana"]
# b=fruit["apple"]*strock["apple"]
# c=fruit["orange"]*strock["orange"]
# d=fruit["pear"]*strock["pear"]
tong=tong+a

print("the price:",tong)
 