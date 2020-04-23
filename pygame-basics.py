import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 500))

# rgb format
# primary colours - red green blue
# rgb value 0-255
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
screen.fill(white)
x = 100
y = 100
moveX = 2
moveY = 1

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()

    screen.fill(white)
    # surface, color, (x,y), radius
    pygame.draw.circle(screen, green, (x, y), 50)
    x += moveX
    # y += 1
    y += moveY

    if y > 500:
        # y -= 1
        moveY = -1
    if x > 1000:
        moveX = -2

    pygame.display.update()
