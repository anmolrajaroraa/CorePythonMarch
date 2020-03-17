Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1 + 3
4
>>> a = 10
>>> #dynamic typing
>>> a = "ten"
>>> print(a)
ten
>>> a = 10
>>> a
10
>>> a = "ten"
>>> a
'ten'
>>> a = ten
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a = ten
NameError: name 'ten' is not defined
>>> 
>>> ten = 10
>>> 10 = "x"
SyntaxError: can't assign to literal
>>> a = "ten"
>>> 
>>> a = 10
>>> type
<class 'type'>
>>> print
<built-in function print>
>>> type(a)
<class 'int'>
>>> 1. Integer
SyntaxError: invalid syntax
>>> #  1. Integer
>>> True
True
>>> False
False
>>> None
>>> a = -2424252525256662662
>>> type(a)
<class 'int'>
>>> a = -2424252525256662662.2
>>> type(a)
<class 'float'>
>>> #  2. float (floating point numbers - numbers having decimal places)
>>> 
>>> a = 3 / 10
>>> a
0.3
>>> a = 3 // 10
>>> a
0
>>> a = 399 / 10  #classic division
>>> a
39.9
>>> a = 399 // 10  #floor division
>>> a
39
>>> round(39.9)
40
>>> a = 3 / 10
>>> type(a)
<class 'float'>
>>> a = 3 // 10
>>> type(a)
<class 'int'>
>>> 
>>> a = 'hello'
>>> type(a)
<class 'str'>
>>> # string (str / text)
>>> # boolean -> True / False
>>> 
>>> a = True
>>> a
True
>>> type(a)
<class 'bool'>
>>> a = true
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a = true
NameError: name 'true' is not defined
>>> a = "true"
>>> a = "True"
>>> type(a)
<class 'str'>
>>> a = None
>>> print(a)
None
>>> type(a)
<class 'NoneType'>
>>> 2 * 8
16
>>> 2 ** 8
256
>>> 8 ** 2
64
>>> pow(8,2)
64
>>> a = 10 + i10
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a = 10 + i10
NameError: name 'i10' is not defined
>>> a = complex( 10, 25 )
>>> a
(10+25j)
>>> a.real
10.0
>>> a.imag
25.0
>>> #internationalization
>>> 
>>> # character -> 1 byte -> 256 unique values -> 00000011 -> 8 bits ->
>>> 2 ** 8
256
>>> 2 ** 16
65536
>>> 2 ** 24
16777216
>>> 
>>> x = 'a'
>>> ord(x) #ordinal - ascii code
97
>>> chr(97)
'a'
>>> chr(65)
'A'
>>> chr(40)
'('
>>> name = "राम कुमार "
>>> print(name)
राम कुमार 
>>> name.encode()
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae \xe0\xa4\x95\xe0\xa5\x81\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xb0 '
>>> name = "राम कुमार sharma"
>>> name.encode()
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae \xe0\xa4\x95\xe0\xa5\x81\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xb0 sharma'
>>> m = name.encode()
>>> print(m)
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae \xe0\xa4\x95\xe0\xa5\x81\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xb0 sharma'
>>> m.decode()
'राम कुमार sharma'
>>> ord("र")
2352
>>> chr(2351)
'य'
>>> num = 1234
>>> bin(1234)
'0b10011010010'
>>> bin(10)
'0b1010'
>>> bin('0b10')
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    bin('0b10')
TypeError: 'str' object cannot be interpreted as an integer
>>> bin(number = 10)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    bin(number = 10)
TypeError: bin() takes no keyword arguments
>>> bin(10)
'0b1010'
>>> print("hello world")
hello world
>>> print("hello world", end="..")
hello world..
>>> oct(1234)
'0o2322'
>>> oct_number = oct(1234)
>>> otc_number
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    otc_number
NameError: name 'otc_number' is not defined
>>> oct_number
'0o2322'
>>> type(oct_number)
<class 'str'>
>>> hex(1234)
'0x4d2'
>>> num = '0x4d2'
>>> num
'0x4d2'
>>> num = int('0x4d2')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    num = int('0x4d2')
ValueError: invalid literal for int() with base 10: '0x4d2'
>>> num = int(0x4d2)
>>> num
1234
>>> num = int(4d2)
SyntaxError: invalid syntax
>>> num = int(1010)
>>> num
1010
>>> num = int(0b1010)
>>> int(0b1010)
10
>>> int(0o1010)
520
>>> int(0x1010)
4112
>>> a = 10
>>> type(a)
<class 'int'>
>>> type(10)
<class 'int'>
>>> id(a)
4354362832
>>> a = None
>>> a
>>> a = 10
>>> id(a)
4354362832
>>> hex(id(a))
'0x1038a4dd0'
>>> b = 10
>>> c = 20 #   = is assignment operator
>>> #   == -> comparison operator
>>> 
>>> b == c
False
>>> a == b
True
>>> hex(id(a))
'0x1038a4dd0'
>>> hex(id(b))
'0x1038a4dd0'
>>> x = "hello this is java programming"
>>> y = "hello this is java programming"
>>> hex(id(a))
'0x1038a4dd0'
>>> hex(id(x))
'0x106a4f5d0'
>>> hex(id(y))
'0x106a4f710'
>>> x == y
True
>>> hex(id(x)) == hex(id(y))
False
>>> type(10)
<class 'int'>
>>> dir(10)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 
>>> dir("abc")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> "abc".__len__()
3
>>> len("abc")
3
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/core-python-march/print_demo.py", line 1, in <module>
    abc + 1
NameError: name 'abc' is not defined
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/core-python-march/print_demo.py", line 7, in <module>
    print("Sum of " + a + " and " +  b + " is " + c)
TypeError: can only concatenate str (not "int") to str
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/core-python-march/print_demo.py", line 8, in <module>
    print("Sum of " + a + " and " +  b + " is " + c)
TypeError: can only concatenate str (not "int") to str
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30
helloworld
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/core-python-march/print_demo.py", line 11, in <module>
    print("Sum of " + a + " and " +  b + " is " + c)
TypeError: can only concatenate str (not "int") to str
>>> 
>>> a = 10
>>> str
<class 'str'>
>>> str(a)
'10'
>>> bool(a)
True
>>> bool(0)
False
>>> float(a)
10.0
>>> name = "ram"
>>> int(name)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    int(name)
ValueError: invalid literal for int() with base 10: 'ram'
>>> ord("ram")
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    ord("ram")
TypeError: ord() expected a character, but string of length 3 found
>>> ord("r")
114
>>> ord("a")
97
>>> ord("m")
109
>>> bool(name)
True
>>> bool("")
False
>>> bool(None)
False
>>> int(None)
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    int(None)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
>>> str(None)
'None'
>>> num = 10.2
>>> int(num)
10
>>> num = 10.9
>>> int(num)
10
>>> #  int(num) #gives the floor value
>>> str(num)
'10.9'
>>> bool(num)
True
>>> int(True)
1
>>> int(False)
0
>>> str(True)
'True'
>>> str(False)
'False'
>>> float(True)
1.0
>>> float(False)
0.0
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30
helloworld
Sum of a and b is c
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30
helloworld
Sum of 10 and 20 is 30
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30
helloworld
Sum of 10 and 20 is 30
Sum of 10 and 20 is 30
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30.2
helloworld
Sum of 10.2 and 20 is 30.2
Sum of 10 and 20 is 30
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30.2
helloworld
Sum of 10.2 and 20 is 30.2
Sum of 10.200000 and 20 is 30
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30.2
helloworld
Sum of10.2and20is30.2
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30.2
helloworld
Sum of10.2and20is30.2
Sum of 10 and 20 is 30
Sum of 10.2 and 20 is 30.2
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30.2
helloworld
Sum of10.2and20is30.2
Sum of 10 and 20 is 30
Sum of 10.2 and 20 is 30.2
Sum of 10.2 and 20 is 30.2
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30.2
helloworld
Sum of10.2and20is30.2
Sum of 10 and 20 is 30
Sum of 10.2 and 20 is 30.2
Sum of 10.2 and 20 is 30.2
Sum of 10.2 and 20 is 30.2. diff of 10.2 and 20 is -9.8. product of 10.2 and 20 is 204.0
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30.2
helloworld
Sum of10.2and20is30.2
Sum of 10 and 20 is 30
Sum of 10.2 and 20 is 30.2
Sum of 10.2 and 20 is 30.2
Sum of 10.2 and 20 is 30.2. diff of 10.2 and 20 is -9.8. product of 10.2 and 20 is 204.0
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30.2
helloworld
Sum of10.2and20is30.2
Sum of 10 and 20 is 30
Sum of 10.2 and 20 is 30.2
Sum of 10.2 and 20 is 30.2
Sum of 10.2 and 20 is 30.2. diff of 10.2 and 20 is -9.8. product of 10.2 and 20 is 204.0
Sum of 10.2 and 20 is 30.2. diff of 10.2 and 20 is -9.8. product of 10.2 and 20 is 204.0
Sum of {a} and {b} is {c}. diff of {a} and {b} is {a-b}. product of {a} and {b} is {a*b}
>>> 
== RESTART: /Users/anmolrajarora/Documents/core-python-march/print_demo.py ==
hello world
30.2
helloworld
Sum of10.2and20is30.2
Sum of 10 and 20 is 30
Sum of 10.2 and 20 is 30.2
Sum of 10.2 and 20 is 30.2
Sum of 10.2 and 20 is 30.2. diff of 10.2 and 20 is -9.8. product of 10.2 and 20 is 204.0
Sum of 10.2 and 20 is 30.2. diff of 10.2 and 20 is -9.8. product of 10.2 and 20 is 204.0
Sum of 10.2 and 20 is 30.2. diff of 10.2 and 20 is -9.8. product of 10.2 and 20 is 204.0
>>> 
