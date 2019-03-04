from turtle import *
x=["red","black","blue","yellow","pink"]

for i in range(0,5,1):
    color(x[i])
    begin_fill()
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    penup()
    forward(50)
    end_fill()

mainloop()