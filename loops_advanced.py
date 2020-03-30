list1 = [[123, 34], [45, 73, 6], [7, 236, 689]]

# for i in [0, 1, 2, 3, 4, 5, 6, 7]:
#     print(list1[i])

# print("************************************************************")

# for element in list1:
#     print(element)

for inner_list in list1:
    for element in inner_list:
        print(element)

employee = {
    "e_id": 101,
    "name": "Ram Kumar",
    "salary": 25000,
    "contact": [1234, 5678],
    "addresses": {
            "home": "Rohini",
            "office": "NSP"
    }
}

print("************************************************************")

for x in employee.keys():
    print(f"{x} : {employee[x]}")

for item in employee.items():
    print(item)

for value in employee.values():
    print(value)

'''
Score -> player , cpu , draw, totalMatches
user input -> stone paper scissors
choices = []
if user_input not in choices:
cpu_input
if_else conditions
7 conditions
'''
