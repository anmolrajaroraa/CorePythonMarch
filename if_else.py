num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number : "))

'''
if(num_1 > num_2){
    print("Num1 is greater than Num2")
}
'''

if num_1 > num_2:
    print("num1 is", num_1)
    print("num2 is", num_2)
    print("num1 is greater than num2")
elif num_1 < num_2:
    print("num1 is", num_1)
    print("num2 is", num_2)
    print("num1 is lesser than num2")
else: print("num1 is equal to num2")
print("If condition ran....")
