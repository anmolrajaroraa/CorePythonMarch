def takeInput():
    first_num = int(input("Enter first number : "))
    second_num = int(input("Enter second number : "))
    return first_num, second_num


def add():
    x, y = takeInput()
    print(x + y)


def subtract():
    x, y = takeInput()
    print(x - y)


def multiply():
    x, y = takeInput()
    print(x * y)


def divide():
    x, y = takeInput()
    print(x / y)


def calculateAll():
    x, y = takeInput()
    print(x + y, x - y, x * y, x / y)


def errorHandler():
    print("Invalid choice!")


print('''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. CalculateAll
''')
choice = int(input("Enter your choice : "))
options = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide,
    5: calculateAll
}
# options[choice](first_num, second_num)
options.get(choice, errorHandler)()
