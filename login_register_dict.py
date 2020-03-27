users = [
    {
        "username": "Ram Kumar",
        "email": "ram@gmail.com",
        "password": "ram123"
    }
]

while True:
    print('''
    1. Login
    2. Register
    3. Exit
    ''')
    choice = int(input("Enter your choice : "))
    if choice > 3 or choice < 1:
        print("Wrong choice!!")
        continue
    elif choice == 3:
        print("Thank you. See you again!")
        break
    elif choice == 2:
        name = input("Enter your name : ")
        email = input("Enter your email : ")

        userFound = False

        for i in range(len(users)):
            user_dict = users[i]
            if email == user_dict["email"]:
                userFound = True
                print("Account already exists! Please try to login!")
                break

        if not userFound:
            password = input("Enter your password : ")
            user_dict = {
                "username": name,
                "email": email,
                "password": password
            }
            users.append(user_dict)
            print("Registeration successful !")
            print(users)
