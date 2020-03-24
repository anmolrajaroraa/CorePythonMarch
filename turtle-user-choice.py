import turtle

screen = turtle.Screen()
screen.bgcolor('black')

fred = turtle.Pen()
fred.pendown()
'''fred.speed(3)
fred.shape('turtle')
fred.turtlesize(3)
fred.width(3)
fred.color('yellow')'''

while True:

    fred.reset()
    fred.speed(3)
    fred.shape('turtle')
    fred.turtlesize(3)
    fred.width(3)
    fred.color('yellow')

    shape = input("Which shape do you want to see ? ")
    
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
    elif shape == "octagon":
        for i in range(8):
            fred.forward(100)
            fred.left(45)
    else:
        print("Didn't understand!")
        continue

    choice = input("Do you want to continue : ")
    if choice == "no":
        break
                   
