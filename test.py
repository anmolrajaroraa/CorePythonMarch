users = [
    {"username": "Ram",
     "email": "ram@gmail.com",
     "password": "1111"}
]
while True:
    print("Do you want to \n1.Login\n2.Signup\n3.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        umail = input("Enter Email: ")
        for i in range(len(users)):
            userconfirm = users[i]
            if umail == userconfirm["email"]:
                upwd = input("Enter password: ")
                if upwd == userconfirm["password"]:
                    print("Login Successful")
                else:
                    print("Wrong Password")
                break
        else:
            print("Email does not exist. please Signin")
    elif choice == "2":
        Nname = input("Enter user name: ")
        Nmail = input("Enter valid email:")
        if Nmail == userconfirm["email"]:
            print("Email already exists. Please Login")
        else:
            Npwd = input("Enter password: ")
            Ncpwd = input("Confirm password: ")
            if Npwd == Ncpwd:
                userdict = {
                    "username": Nname,
                    "email": Nmail,
                    "password": Npwd
                }
                users.append(userdict)
                print("Signup Successful. Please Login")
                print(users)
            else:
                print("Passwords do not match")
    elif choice == "3":
        print("Hope to see you again")
        break
    else:
        print("Please chose the correct option")
