import turtle

screen = turtle.Screen()
screen.bgcolor('black')

fred = turtle.Pen()
fred.speed(0)
fred.width(3)
fred.shape('turtle')
fred.turtlesize(2)
fred.color("yellow")
fred.penup()
fred.setposition(0, -100)
fred.pendown()

for i in range(50):
    fred.circle(10 + (i * 5) )
    fred.left(10)
