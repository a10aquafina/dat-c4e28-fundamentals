from random import*
x=[-1,6,10,1,-6]

# print(len(x))
number=[]


for i in range(len(x)):
    a=choice(x)
    
    b=a%2
    if b==0 and a>0:
        
        number.append(a)
        x.remove(a)
print(number)




