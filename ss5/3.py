from turtle import*
def draw_square(x,y,z):
    color(z)
    for i in range(4):
        forward(x)
        left(90)
draw_square(100,100,"red")