import random

player1Wins = 0
player2Wins = 0
drawMatches = 0

gameChoices = ['stone', 'paper', 'scissors']

print('''
    1. 1-Player game
    2. 2-Player game
    ''')

whoIsPlayer2 = None

while True:
    gameType = int(input("Which game type do you want to play: "))
    if gameType == 1:
        whoIsPlayer2 = "cpu"
        break
    elif gameType == 2:
        whoIsPlayer2 = "player2"
        break
    else:
        print("Invalid choice")


while True:
    if player1Wins == 3:
        print("Player 1 won the game!!")
        break
    elif player2Wins == 3:
        print("Player 2 won the game!!")
        break

    while True:
        player1Choice = input("Player 1 turn: ")
        # print("Player1 choice is " + player1Choice)
        if player1Choice in gameChoices:
            print("Valid choice")
            break
        else:
            print("Invalid choice")

    if whoIsPlayer2 == "cpu":
        player2Choice = random.choice(gameChoices)
        print(player2Choice)
        # print("Cpu choice is ", player2Choice)
    else:
        while True:
            player2Choice = input("Player 2 turn: ")
            # print("Player2 choice is " + player2Choice)
            if player2Choice in gameChoices:
                print("Valid choice")
                break
            else:
                print("Invalid choice")

    if player1Choice == player2Choice:
        print("Game draw")
        drawMatches += 1

    if player1Choice == "stone":
        if player2Choice == "paper":
            # print("User lost")
            player2Wins += 1
        else:
            # print("User won")
            player1Wins += 1

    elif player1Choice == "paper":
        if player2Choice == "stone":
            # print("User won")
            player1Wins += 1
        else:
            # print("User lost")
            player2Wins += 1
    else:
        if player2Choice == "stone":
            # print("User lost")
            player2Wins += 1
        elif player2Choice == "paper":
            # print("User won")
            player1Wins += 1

    print(
        f"Score -> Player1 : {player1Wins}, Player2 : {player2Wins}, Draw : {drawMatches}, Total Matches Played : {player1Wins + player2Wins + drawMatches} ")
