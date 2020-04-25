import pygame
import random
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
moveX = 0
moveY = 0
x2 = random.randint(0, 950)
y2 = random.randint(0, 450)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0

    screen.fill(white)
    # surface, color, (x,y), radius
    # pygame.draw.circle(screen, green, (x, y), 50)

    #scree, color, (x,y,length,breadth)
    rect1 = pygame.draw.rect(screen, blue, (x, y, 50, 50))
    rect2 = pygame.draw.rect(screen, red, (x2, y2, 50, 50))
    x += moveX
    # y += 1
    y += moveY

    if rect1.colliderect(rect2):
        x2 = random.randint(0, 950)
        y2 = random.randint(0, 450)

    # if y > 450:
    #     # y -= 1
    #     moveY = -1
    # elif x > 950:
    #     moveX = -1
    # elif x < 50:
    #     moveX = 1
    # elif y < 50:
    #     moveY = 1

    # if x < 0:
    #     moveX = 1
    # elif y < 0:
    #     moveY = 1
    # elif x > 900:
    #     moveX = -1
    # elif y > 400:
    #     moveY = -1

    if x > 1000:
        x = -50
    elif y > 500:
        y = -50
    elif x < -50:
        x = 1000
    elif y < -50:
        y = 500

    pygame.display.update()
