list1 = [35, 65, 24, 6, [87, 35, 677], [8, 100, 12], 8]
list_containing_numbers = []
list_containing_lists = []

for i in range(len(list1)):
    element = list1[i]
    if type(element) == int:
        # print(element)
        list_containing_numbers.append(element)
    else:
        # for j in range(len(element)):
        #     print(element[j])
        element.sort()
        list_containing_lists.append(element)

list_containing_lists.sort()
list_containing_numbers.sort()
list_containing_numbers.extend(list_containing_lists)
print(list_containing_numbers)
