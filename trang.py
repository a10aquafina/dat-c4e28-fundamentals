
# j=True
# while j:
# n , s = [int(x) for x in input("Enter two value: ").split()] 
# print() 
    # if n>=1 and s<= 10**18:
    #     j=False
x,y=int(input("nhap vao")).split
m=n
tong1=0
i=True
while i:
    du=n%10
    tong1 = tong1 + du
    n=(n-du)/10
    print("tong 1 la: ",tong1)
    print("n la: ",n)
    if n<=0:
        end=m-tong1
        if end>=s:
            print(m-s)
        else:
            print(m-m)
