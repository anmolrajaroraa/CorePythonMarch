# def fn_name (arg1, arg2, arg3..., argn)
def add():
    print(first_num + second_num)
    return None
    print("Statement after return")  # Unreachable code


def add2(x, y):
    print("Add2 called")
    print(x + y)


def add3(x, y=1):  # default argument
    print("Add3 called..")
    print(x + y)


def add4(x=1, y=1):
    print("Add4 called..")
    print(x + y)


def subtract(x, y):
    # print(x - y)
    return x - y


def multiply(x, y):
    print(x * y)


def divide(x, y):
    print(x / y)


def calculateAll(x, y):
    return x + y, x - y, x * y, x / y  # packing


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
if choice == 1:
    # add(first_num, second_num)
    result = add()
    print("Result is ", result)
    # add2(10, 20)
    add3(10, 20)
    add3(10)
    add4(10, 20, 30)
    add4(10)
    add4()
elif choice == 2:
    result = subtract(first_num, second_num)
    print("Result is ", result)
elif choice == 3:
    multiply(first_num, second_num)
elif choice == 4:
    divide(first_num, second_num)
elif choice == 5:
    result = calculateAll(first_num, second_num)
    print(result)
    a, b, c, d, *e = calculateAll(first_num, second_num)  # unpacking
    print(f"a = {a}, b is {b}, c is {c}, d is {d}, e is {e}")
    a, b, c, d, e = calculateAll(first_num, second_num)
else:
    print("Invalid choice..")

# *c -> *args -> gives us a list of leftover values after unpacking (varargs) - variable arguments
# if we use single variable while unpacking, then we get a tuple of
# result = calculateAll(first_num, second_num)
