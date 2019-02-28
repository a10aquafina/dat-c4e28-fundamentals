m=int(input("dien can nang"))
h=int(input("dien chieu cao"))
if h>10:
    h1=h/100
else:
    h1=h
    
BMI = m/(h1*h1)
if BMI<16:
    print("thieu can nghiem trong")
if 16<BMI<18.5:
    print("thieu can")
if 18.5<BMI<25:
    print("binh thuong")
if 25<BMI<30:
    print("thua can")
if BMI>30:
    print("beo phi")
