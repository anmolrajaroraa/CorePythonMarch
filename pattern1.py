'''
*
**
***
****
*****
'''

'''for i in range(5):
    for j in range(i + 1):
        #print("*", end='\n')
        print("*", end='')
    print()'''

'''for i in range(5):
    print("*" * (i + 1), end="")'''
#string multiplication

'''
    *
   **
  ***
 ****
*****
'''

'''
*****
****
***
**
*
'''
'''
    *
   ***
  *****
 *******
*********
'''

print("*****Diamond********")

for i in range(5):
    for j in range(4 - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
for i in range(4):
    for j in range(i + 1):
        print(" ", end="")
    for k in range(7 - (2 * i)):
        print("*", end="")
    print()


print("----------------")

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

for i in range(5):
    for j in range(i):
        print(" ", end='')
    for k in range(5 - i):
        print("*", end='')
    print()

print("----------------")

for i in range(5):
    print(" " * i, end='')
    print("*" * (5 - i) )


for i in range(5): print(i)

for i in range(5): print(" "*i, "*"*(5-i), sep="")


'''
*****
 ****
  ***
   **
    *
'''

'''
>>> print("hello")
hello
>>> print("hello","world")
hello world
>>> print("hello","world", sep="&")
hello&world
>>> print("hello","this","is","python","prog.", sep="&")
hello&this&is&python&prog.
>>> print("hello","this","is","python","prog.", sep="")
hellothisispythonprog.
'''
