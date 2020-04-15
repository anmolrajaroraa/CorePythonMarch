def add(x, y):
    print(x + y)
    break


def subtract(x, y):
    print(x - y)


def multiply(x, y):
    print(x * y)


def divide(x, y):
    print(x / y)


def calculateAll(x, y):
    print(x + y, x - y, x * y, x / y)


print('''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. CalculateAll
''')
choice = int(input("Enter your choice : "))
first_num = int(input("Enter first number : "))
second_num = int(input("Enter second number : "))
options = {
    1: add(first_num, second_num),
    2: subtract(first_num, second_num),
    3: multiply(first_num, second_num),
    4: divide(first_num, second_num),
    5: calculateAll(first_num, second_num)
}
options[choice]
