from turtle import*

def koch(order,length):
    if order==0:
        forward(length)
    else:
        for angle in [60,-120,60,0]:
            koch(order-1,length/3)
            left(angle)

window=Screen()
window.setup(width=600,height=600)
speed('fastest')

penup()
goto(-window.window_width()/2,0)
pendown()

koch(5,600)

hideturtle()
mainloop()