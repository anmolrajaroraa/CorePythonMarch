import pygame
pygame.init()

width = 1000
height = 400

screen = pygame.display.set_mode((width, height))

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
noOfBricks = 10
totalWidthAvailableForBricks = width - 10  # 790
perBrickWidthAvailable = totalWidthAvailableForBricks / noOfBricks  # 79
widthAvailableAfterRemovingGap = perBrickWidthAvailable - 10
barX = (width // 2) - 125
barY = 360
ballY = 350
barMoveX = 0
ballMoveX = 0
ballMoveY = 0
isSpaceBarPressed = False
ballX = barX + 125

bricks = []

for i in range(noOfBricks):
    for j in range(4):
        # bricks.append([10 + (i * perBrickWidthAvailable), 10 + (j * 35)])
        bricks.append(pygame.Rect(
            (10 + (i * perBrickWidthAvailable), 10 + (j * 35), widthAvailableAfterRemovingGap, 25)))

print(bricks)
print(len(bricks))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                barMoveX = 2
            if event.key == pygame.K_LEFT:
                barMoveX = -2
            if event.key == pygame.K_SPACE:
                ballMoveX = 2
                ballMoveY = -2
                isSpaceBarPressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                barMoveX = 0
            if event.key == pygame.K_LEFT:
                barMoveX = 0

    screen.fill(white)

    for brick in bricks:
        pygame.draw.rect(screen, green, brick)

    # pygame.draw.rect(screen, green, (10, 10, 780, 25))

    # 10, 89, 168

    pygame.draw.rect(screen, blue, (barX, barY, 250, 15))

    pygame.draw.circle(screen, red, (ballX, ballY), 10)

    rectForBall = pygame.Rect((ballX, ballY, 10, 10))

    for i in range(len(bricks)):
        if rectForBall.colliderect(bricks[i]):
            ballMoveY = 2
            del bricks[i]
            break

    barX += barMoveX
    if isSpaceBarPressed:
        ballX += ballMoveX
    else:
        ballX = barX + 125
    ballY += ballMoveY

    pygame.display.update()
