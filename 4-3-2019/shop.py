y=["T Shirt","Sweat"]
print(*y,sep=(","))
print("What do you want?delete or plus item")
print("if u want to delete,u can fill 0.if not enter 1 ")
i=int(input("i want "))
if i==1:
    x=input("Enter the item")

    y.append(x)
    print(*y,sep=",")
else:
    x=input("i want to delete:")
    if len(x)==5:
        del y[1]
    else:
        del y[0]
print(*y,sep=",")        