print("hello world")

a = 10.2
b = 20
c = a + b
d = "hello" + "world"
b
print(c)
print(d)

#print("Sum of " + 'a' + " and " +  'b' + " is " + 'c')
print("Sum of" + str(a) + "and" +  str(b) + "is" + str(c))

print("Sum of %d and %d is %d"%(a,b,c) )
# %d -> decimal number
# %f -> float number
# %s -> string

'''Benefits
1. No type casting required
2. No need to take care of spaces
3. Only use commas instead of +   '''
print("Sum of", a, "and",  b, "is", c)

print("Sum of {} and {} is {}".format(a,b,c) )

print("Sum of {} and {} is {}. diff of {} and {} is {}. product of {} and {} is {}".format(a,b,c,a,b,a-b,a,b,a*b) )

print("Sum of {0} and {1} is {2}. diff of {0} and {1} is {4}. product of {0} and {1} is {3}".format(a,b,c,a*b,a-b) )

#f-strings (fast, format)
print(f"Sum of {a} and {b} is {c}. diff of {a} and {b} is {a-b}. product of {a} and {b} is {a*b}")

#print( f" {a=} {b=} {c=}" )

'''
>>> a = 10
>>> b = 20
>>> c = 30
>>> print( f" {a=} {b=} {c=}" )
 a=10 b=20 c=30
>>> c = a+b
>>> print( f" {a=} {b=} {c=}" )
 a=10 b=20 c=30
>>> a = "ten"
>>> print( f" {a=} {b=} {c=}" )
 a='ten' b=20 c=30
>>> '''



