import csv
users = [
    {
        "username": "ram",
        "email": "ram@gmail.com",
        "password": "ram1234"
    },
    {
        "username": "shyam",
        "email": "shyam@gmail.com",
        "password": "shyam1234"
    },
    {
        "username": "mohan",
        "email": "mohan@gmail.com",
        "password": "mohan1234"
    },
    {
        "username": "anna",
        "email": "anna@gmail.com",
        "password": "anna123"
    },
    {
        "username": "jenny",
        "email": "jenny@gmail.com",
        "password": "jenny123"
    }
]


# csv - comma separated values


# with open("users.csv", "a") as fileStream:
# writer = csv.writer(fileStream)
#     # writer.writerow(("ram", "ram@gmail.com", "ram1234"))
#     for user in users:
#         writer.writerow(user.values())

with open("users.csv", "r", newline="") as fileStream:
    reader = csv.reader(fileStream)
    for row in reader:
        print(row)
