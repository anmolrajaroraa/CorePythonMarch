Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1 + 2
3
>>> 1 - 2
-1
>>> 1 / 2
0.5
>>> 1 * 2
2
>>> 22/7
3.142857142857143
>>> round(22/7)
3
>>> 22 // 7
3
>>> 10 * 2
20
>>> 10 ** 3
1000
>>> 2 ** 9
512
>>> pow(2,9)
512
>>> print( "hello" )  #pass text as an argument
hello
>>> print
<built-in function print>
>>> print( "hello world" )  #pass text as an argument
hello world
>>> print( 100 )
100
>>> #data types
>>> #int (integer - numbers without decimals)
>>> # float (floating point numbers)
>>> #bool (boolean - yes / no - 1/ 0 - true / false)
>>> true
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> true = 10
>>> true
10
>>> 10
10
>>> True
True
>>> False
False
>>> #str (string - text - 'text' - "text")
>>> 'hello'
'hello'
>>> "hello"
'hello'
>>> #ascii table 256 characters -> 0 - 255
>>> राम
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    राम
NameError: name 'राम' is not defined
>>> "राम"
'राम'
>>> print("राम")
राम
>>> name = "राम"
>>> print(name)
राम
>>> name.encode()
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae'
>>> name = "राम kumar"
>>> name.encode()
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae kumar'
>>> x = name.encode()
>>> x
b'\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae kumar'
>>> type(x)
<class 'bytes'>
>>> type("राम")
<class 'str'>
>>> name = "ram कुमार"
>>> name.encode()
b'ram \xe0\xa4\x95\xe0\xa5\x81\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xb0'
>>> 
>>> x = name.encode()
>>> x
b'ram \xe0\xa4\x95\xe0\xa5\x81\xe0\xa4\xae\xe0\xa4\xbe\xe0\xa4\xb0'
>>> x.decode()
'ram कुमार'
>>> a = 10 + i5
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a = 10 + i5
NameError: name 'i5' is not defined
>>> a = "10 + i5"
>>> type(a)
<class 'str'>
>>> a = 10 + 5i
SyntaxError: invalid syntax
>>> a = 5i + 10
SyntaxError: invalid syntax
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = 10.2
>>> type(a)
<class 'float'>
>>> ord('a')
97
>>> chr(50)
'2'
>>> #ordinal -> ascii value related to character
>>> #chr() -> gives us the character related to the ascii code provided
>>> m = complex(10,5)
>>> m
(10+5j)
>>> m.real
10.0
>>> m.imag
5.0
>>> 
