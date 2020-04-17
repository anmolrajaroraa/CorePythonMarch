def even(num):
    return num % 2 == 0


# lambda fns, anonymous fns, single line fns
# print(even(11))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in list1:
    print(even(num))

result = map(even, list1)
print(list(result))

result2 = map(lambda num: num % 2 == 0, list1)
print(list(result2))

# any fn can be written as lambda expression if it contains a single statement that returns something
# map fn calls the given fn or lambda for each value in list and gives the result as a list

result3 = filter(lambda num: num % 2 == 0, list1)
print(list(result3))
# filter fn works just like map, but it works only for fns that return boolean values and instead of returning boolean values it gives us back the argument whenever the return value is true
