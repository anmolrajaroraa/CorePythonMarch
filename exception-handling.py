# try:
#     a = int(input("Enter first number : "))
#     b = int(input("Enter second number : "))

#     q = a / b

#     print("Quotient is ", q)
# except ValueError:
#     print("Please enter only integers")
# except ZeroDivisionError:
#     print("Please dont enter 0 as second number")
# except BaseException as err:
#     print("Some error occured")
#     print("error is", err)

# import io
# import os

try:
    path = "file-handling-xyz.txt"
    with open(path) as fileStream:
        fileStream.read()
# except FileNotFoundError:
#     print("Please check that file already exists...")
# except io.UnsupportedOperation:
#     print("You cannot write when file is in read mode...")
except BaseException as err:
    print("Some error occured")
#     print("error is", err)
# else:
#     print("File read successfully....")
finally:
    #     if(os.path.isfile(path)):
    fileStream.close()
# databaseConnection.close()

# try block is used to run code and check for any exceptions
# except <exception-class> is used for handling diff types of exceptions
# finally block - it will run always (exception occurs or not) at the end


balance = 10000


def withdraw():
    global balance
    pin = 1234
    pinInput = int(input("Please enter PIN: "))
    # if pinInput != pin:
    #     print("Incorrect PIN")
    #     raise ValueError("Pin was not correct")

    assert(pin == pinInput), "Pin incorrect"

    amount = int(input("Enter the amount you want to withdraw: "))
    # if amount > balance:
    #     print("Insufficient balance")
    #     raise ValueError("Balance is not enough")

    assert amount <= balance, "Insufficient balance"
    balance -= amount
    print("Updated balance is", balance)


def checkBalance():
    print("Current balance is", balance)


try:
    withdraw()
    checkBalance()
except AssertionError as err:
    print(err)
except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
except BaseException as err:
    print(err)
else:
    print("Thank you for visiting!")
