from turtle import*
def draw_square(x,y):
    color(y)
    
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
