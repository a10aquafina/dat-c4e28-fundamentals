x=[5,7,300,90,24,50,75,100]
print(*x,sep=",")
c=list(x)
b=max(list(x))
print("the biggest ship",b)
month=0
y=int(input("enter the number of month "))
month=month+y

x[0]=x[0]+50*y
x[1]=x[1]+50*y
x[2]=x[2]+50*y
x[3]=x[3]+50*y
x[4]=x[4]+50*y
x[5]=x[5]+50*y
x[6]=x[6]+50*y
x[7]=x[7]+50*y
if x[0]>300:
    x[0]=8
if x[1]>300:
    x[1]=8
if x[2]>300:
    x[2]=8
if x[3]>300:
    x[3]=8
if x[4]>300:
    x[4]=8
if x[5]>300:
    x[5]=8
if x[6]>300:
    x[6]=8
if x[7]>300:
    x[7]=8
print(x)
money=0
f=sum(list(x))
money=money+f*2
print("the size ship:",f)
print("your monney:", money)








    
