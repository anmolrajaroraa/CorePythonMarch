import turtle

#Screen and Pen are classes, therefore the name should start with a capital letter

screen = turtle.Screen()
screen.bgcolor('black')

fred = turtle.Pen()
fred.pendown()
fred.speed(3)
fred.shape('turtle')
fred.turtlesize(3)
fred.width(3)
fred.color('yellow')

for i in range(4):
    fred.forward(200)
    fred.left(90)
fred.left(90)
fred.forward(200)
fred.write("Square", False, "left", ("Arial", 30, "normal"))
fred.circle(50.9)  #radius
fred.dot(50)  #diameter
fred.hideturtle()


'''fred.forward(200)
fred.left(90)
fred.forward(200)
fred.left(90)
fred.forward(200)
fred.left(90)
fred.forward(200)
fred.left(90)'''

