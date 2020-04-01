import random

userWins = 0
cpuWins = 0
drawMatches = 0

gameChoices = ["stone", "paper", "scissors"]

while userWins < 3 and cpuWins < 3:

    player_choice = input("Player 1 turn : ")

    if player_choice not in gameChoices:
        print("Wrong choice made!")
        continue

    cpuChoice = random.choice(gameChoices)
    print("CPU choice : " + cpuChoice)

    if player_choice == cpuChoice:
        print("Game Draw")
        drawMatches += 1
    elif player_choice == "stone":
        if cpuChoice == "paper":
            print("Cpu wins")
            cpuWins += 1
        else:
            print("User wins")
            userWins += 1
    elif player_choice == "paper":
        if cpuChoice == "scissors":
            print("Cpu wins")
            cpuWins += 1
        else:
            print("User wins")
            userWins += 1
    elif player_choice == "scissors":
        if cpuChoice == "stone":
            print("Cpu wins")
            cpuWins += 1
        else:
            print("User wins")
            userWins += 1

    print(
        f"Score : User -> {userWins}, CPU -> {cpuWins}, draw -> {drawMatches}, Total Matches -> {userWins + cpuWins + drawMatches}")
