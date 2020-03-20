#choice = ""

#while choice != "no":
while True:
    num = int(input("Enter a number to check for odd and even : " ))

    if num == 0:
        print("Please don't enter 0")
        continue
    elif num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

    choice = input("Do you want to continue ? ")
    if choice == "no":
        break
    
