import pygame
import random
pygame.init()

width = 900
height = 500

screen = pygame.display.set_mode((width, height))

# rgb format
# primary colours - red green blue
# rgb value 0-255
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
screen.fill(white)
# width = 50

bg_music = pygame.mixer.Sound("assets/music_1.wav")
bg_music.play(-1)


def homeScreen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mainScreen()

        # screen.fill(white)

        snake_bg = pygame.image.load("assets/snake_bg.png")
        screen.blit(snake_bg, (0, 0))

        msg = "Press SPACE to Start Game"
        font = pygame.font.SysFont(None, 60)
        text = font.render(msg, True, red)
        screen.blit(text, (180, 450))
        pygame.display.update()


def mainScreen():

    x = 100
    y = 100
    moveX = 0
    moveY = 0
    x2 = random.randint(0, width - 50)
    y2 = random.randint(0, height - 50)
    collisionSound = pygame.mixer.Sound("assets/point.wav")
    counter = 0
    frogImage = pygame.image.load("assets/frog_2.png")
    snakeBody = []
    snakeLength = 1

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 5
                    moveY = 0
                elif event.key == pygame.K_DOWN:
                    moveY = 5
                    moveX = 0
                elif event.key == pygame.K_LEFT:
                    moveX = -5
                    moveY = 0
                elif event.key == pygame.K_UP:
                    moveY = -5
                    moveX = 0

        screen.fill(white)

        scoreText = f"Score : {counter}"
        font = pygame.font.SysFont(None, 30)
        scoreText = font.render(scoreText, True, red)
        screen.blit(scoreText, (20, 20))
        # surface, color, (x,y), radius
        # pygame.draw.circle(screen, green, (x, y), 50)

        #scree, color, (x,y,length,breadth)
        # rect1 = pygame.draw.rect(screen, blue, (x, y, 50, 50))
        # rect2 = pygame.draw.rect(screen, red, (x2, y2, 60, 53))
        rect1 = pygame.Rect((x, y, 50, 50))
        rect2 = pygame.Rect((x2, y2, 60, 53))
        screen.blit(frogImage, (x2, y2))
        x += moveX
        # y += 1
        y += moveY

        snakeBody.append([x, y])
        if len(snakeBody) > snakeLength:
            del snakeBody[0]
        print(snakeBody)

        if rect1.colliderect(rect2):
            x2 = random.randint(0, width - 50)
            y2 = random.randint(0, height - 50)
            collisionSound.play()
            counter += 1
            snakeLength += 5
            # width += 50

        for bodyPart in snakeBody:
            color = random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)
            pygame.draw.rect(screen, color, (bodyPart[0], bodyPart[1], 50, 50))

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

        if x > width:
            x = -50
        elif y > height:
            y = -50
        elif x < -50:
            x = width
        elif y < -50:
            y = height

        pygame.display.update()


homeScreen()
