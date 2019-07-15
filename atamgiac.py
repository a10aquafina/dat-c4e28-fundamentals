n=int(input("nhap so diem "))
dem=0
giatri=[]
tham_so=[]
for i in range(1,n+1,1):
    x , y = [int(x) for x in input("Enter two value: ").split()] 

    tamgiac={
        "x":0,
        "y":0,
    }
    tamgiac["x"]=x
    tamgiac["y"]=y
    giatri.append(tamgiac)

    b=giatri[i-1]["x"]+giatri[i-1]["y"]
    tham_so.append(b)
    print(tham_so)
c=max(tham_so)
print(c)