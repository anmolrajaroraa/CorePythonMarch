# balance = 10000  # global variable


# def outer():
#     global balance  # now balance will be treated as a global variable
#     balance = 5000  # local variable to outer fn
#     print("inside outer fn...", balance)

#     def inner():
#         global balance
#         balance = 4500  # local variable to inner fn
#         print("inside inner fn...", balance)

#     # inner()
#     print("inside outer fn again..", balance)
#     return inner


# result = outer()
# print("Result is", result)
# result()  # inner()
# # outer.inner()
# print("Done all the work...", balance)
# # random.randint()


balance = 10000  # global variable


def outer():
    global balance
    amountWithdrawn = 5000
    balance = balance - amountWithdrawn
    print("inside outer fn...", balance)

    def inner():
        print("inside inner fn...", balance)

    # inner()
    print("inside outer fn again..", balance)
    return inner


result = outer()
print("Result is", result)
result()  # inner()
# outer.inner()
print("Done all the work...", balance)
# random.randint()
