'''while True:
    num = int(input("Enter a number : "))

    isPrime = True

    if(num > 1):
        for i in range(2, num // 2):
            if num % i == 0:
                isPrime = False
                print("Not prime")
                break
        if isPrime:
            print("Prime")
    else:
        print("Please enter number greater than 1")
        continue

    choice = input("Do you want to continue : ")
    if choice == "no":
        break
'''

#if-else -> if the condition in if statement is true then execute the first action
#otherwise execute the action written in else statement

#for-else -> else is an extended block of for loop
#initially, for loop will run on its own and when the for loop ends then else also runs
#but if for loop is broken in between the for loop terminates and since
#else is  part of for loop it is also terminated and never runs

while True:
    num = int(input("Enter a number : "))

    if(num > 1):
        for i in range(2, num // 2):
            if num % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")
    else:
        print("Please enter number greater than 1")
        continue

    choice = input("Do you want to continue : ")
    if choice == "no":
        break
