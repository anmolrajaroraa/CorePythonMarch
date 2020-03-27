'''users = [
    [ "ram@gmail.com", "ram123", "Ram Kumar" ],
    ["raman@gmail.com", "raman123", "Raman Kumar"],
    ["shyam@gmail.com", "shyam123", "shyam Kumar"],
    ["mohan@gmail.com", "mohan123", "Mohan Kumar"]
]

table Users
Username   email    password   age    location   phone

Ram       ram@gmail.com  ram123  24   Delhi   9999'''

users = [
    [ "Ram Kumar", "ram@gmail.com", "ram123" ]
    [ "Shyam Kumar"]
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

        #email in emails

        userFound = False


        for i in range(len(users)):
            user = users[i]
            #if user[1] == ( email := input("Enter your email : ") ):
            if users[i][1] == ( email := input("Enter your email : ") ):
            if user[1] == email:
                userFound = True
                print("Account already exists! Please try to login!")
                break

        if not userFound:
            password = input("Enter your password : ")
            user = [name, email, password]
            users.append(user)
            print("Register successful !")
            print(users)
            #users.append([name, email, password])
            #insert into users values (name, email, password)







'''
Logical operators
a && b -> a and b
a || b -> a or b
!isPrime -> not isPrime

Identity operators
== -> compares objects
is -> compare memory addresses actually saved in the variable
is not -> works opposite of 'is' operator

Membership => IN, NOT IN

Walrus operator
#walrus operator
>>> name = input("Enter your name : " )
Enter your name : Ram
>>> print("Welcome " + name)
Welcome Ram
>>> print("Welcome ", name)
Welcome  Ram
>>> print("Welcome", input("Enter your last name : "))
Enter your last name : Kumar
Welcome Kumar
>>> print("Welcome", lastname = input("Enter your last name : "))
Enter your last name : Kumar
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("Welcome", lastname = input("Enter your last name : "))
TypeError: 'lastname' is an invalid keyword argument for print()
>>> print("Welcome", input("Enter your last name : "), sep = "$")
Enter your last name : kumar
Welcome$kumar
>>> print("Welcome", lastname := input("Enter your last name : "))
Enter your last name : Kumar
Welcome Kumar
>>> lastname
'Kumar'
'''
'''turtle
    Pen
    Screen
    isPrime
    isPrimeOrNot
    AbstractCollection
    is_prime'''
