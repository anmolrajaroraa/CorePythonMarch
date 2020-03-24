import turtle, random

screen = turtle.Screen()
screen.bgcolor('black')

fred = turtle.Pen()
fred.speed(0)
fred.width(3)
fred.shape('turtle')
fred.turtlesize(2)
#fred.color("yellow")

shapes = ["square", "circle", "dot", "rectangle", "triangle", "hexagon", "octagon"]
colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray", "white"]

for i in range(7):

    x = random.randint(-250,250)
    y = random.randint(-250,250)
    fred.penup()
    fred.setposition( x,y )
    fred.pendown()
    
    selectedColor = random.choice(colors)
    fred.color(selectedColor)
    
    shape = random.choice(shapes)
    shapes.remove(shape)
    print(shape)
    
    if shape == "square":
        for i in range(4):
            fred.forward(200)
            fred.left(90)
    elif shape == "circle":
        fred.circle(100)
    elif shape == "dot":
        fred.dot(200)
    elif shape == "triangle":
        for i in range(3):
            fred.forward(200)
            fred.left(120)
    elif shape == "rectangle":
        for i in range(2):
            fred.forward(300)
            fred.left(90)
            fred.forward(200)
            fred.left(90)
    elif shape == "hexagon":
        for i in range(6):
            fred.forward(150)
            fred.left(60)
    else:
        for i in range(8):
            fred.forward(100)
            fred.left(45)
