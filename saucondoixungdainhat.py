from collections import Counter
from random import choice
a=int(input("nhap so luong bo test: "))

# botest=[]
for i in range(a):
    k=input("enter tour word: ")
    b=list(k)
    arandom=[]
    len_b=len(b)
    c=choice(b)
    arandom.append(c)
    b.remove(c)


    table=Counter(b)
    dem=0
    
    str_fred=table.most_common()
    str_fred.sort()
    print("str\tfenque")
    for stri in str_fred:
        print("{0}\t{1}".format(stri[0],stri[1]))
        
        dem=dem+ (stri[1])//2
        a=stri[1]/2
    print("dem: ",dem)
    if a==0:
        print("dem la: ",2*dem)
    else:
        print(2*dem+1)
