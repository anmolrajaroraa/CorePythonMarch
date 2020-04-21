# list1 = []

# for i in range(2, 101, 2):
#     list1.append(i)

# print(list1)

#  [ expression for appending something in the list, for loop, if condition]
#  [ expression for appending something in the list, for loop]


list1 = [i ** 2 for i in range(1, 101) if i % 2 == 0 and i % 3 == 0]
print(list1)

[0, 4, 0, 16, 0, 36, 0, 64, 0, 100, ..., 10000]

# list2 = [i ** 2 for i in range(1, 101) if i % 2 == 0 else 0]
list2 = [i ** 2 if i % 2 == 0 else 0 for i in range(1, 101)]
print(list2)
