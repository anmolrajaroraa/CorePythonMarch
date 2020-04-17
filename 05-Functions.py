def takeInput():
    first_num = input("Enter first number : ")
    second_num = input("Enter second number : ")
    return first_num, second_num


def calculate(operator):
    x, y = takeInput()
    # print(xoperatory)
    print(eval(x + operator + y))


print('''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
''')
choice = int(input("Enter your choice : "))
operators = {
    1: "+",
    2: "-",
    3: "*",
    4: "/"
}
calculate(operators[choice])
