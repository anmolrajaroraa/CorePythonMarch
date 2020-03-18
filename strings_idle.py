Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> input("Enter your name : ")
Enter your name : Ram
'Ram'
>>> name = input("Enter your name : ")
Enter your name : Ram
>>> name
'Ram'
>>> num1 = input("Enter first number : ")
Enter first number : 10
>>> num1
'10'
>>> num1 = int(input("Enter first number : "))
Enter first number : 10
>>> num1
10
>>> num1 = int(input("Enter first number : "))
Enter first number : abc
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    num1 = int(input("Enter first number : "))
ValueError: invalid literal for int() with base 10: 'abc'
>>> num1 = int(input("Enter first number : "))
Enter first number : 10.2
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    num1 = int(input("Enter first number : "))
ValueError: invalid literal for int() with base 10: '10.2'
>>> num1 = float(input("Enter first number : "))
Enter first number : 10.2
>>> num1 = float(input("Enter first number : "))
Enter first number : 10
>>> num1
10.0
>>> input()
True
'True'
>>> bool(input())
True
True
>>> 
>>> type
<class 'type'>
>>> type = "int"
>>> type
'int'
>>> type(num1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    type(num1)
TypeError: 'str' object is not callable
>>> str1 = "hellO this is Python PROgramming"
>>> 
>>> str2 = 'McDonald's'
SyntaxError: invalid syntax
>>> str2 = "McDonald's"
>>> 
>>> str2 = 'The "Incredible" India'
>>> 
>>> str2 = 'The "Incredible" McDonald\'s'
>>> str2
'The "Incredible" McDonald\'s'
>>> print(str2)
The "Incredible" McDonald's
>>> 
>>> 
>>> str1
'hellO this is Python PROgramming'
>>> str1[0]
'h'
>>> str1[1]
'e'
>>> str1[2]
'l'
>>> str1[3]
'l'
>>> str1[4]
'O'
>>> length = len(str1)
>>> str1[ length - 1 ]
'g'
>>> str1[ len(str1) - 1 ]
'g'
>>> str1[-1]
'g'
>>> str1[ -length ]
'h'
>>> str1[ -2 ]
'n'
>>> str1[ -3 ]
'i'
>>> str1[ -4 ]
'm'
>>> str1[ -5 ]
'm'
>>> str1[14]
'P'
>>> str1[14:20]
'Python'
>>> str1[1:20]
'ellO this is Python'
>>> str1[1:20:1]
'ellO this is Python'
>>> str1[1:20:2]
'el hsi yhn'
>>> str1[1:20:3]
'eOh  tn'
>>> str1[1:20:4]
'e s h'
>>> len(str1)
32
>>> str1[21:32]
'PROgramming'
>>> str1[21]
'P'
>>> str1[21:]
'PROgramming'
>>> str1[-1:]
'g'
>>> str1[-1:-10]
''
>>> str1[-1:-10:-1]
'gnimmargO'
>>> str1[-28:-32]
''
>>> str1[-28:-32:-1]
'Olle'
>>> str1[-28:-33:-1]
'Olleh'
>>> str1[-28::-1]
'Olleh'
>>> str1[-11]
'P'
>>> str1[-11:-1]
'PROgrammin'
>>> str1[-11:0]
''
>>> str1[-11:]
'PROgramming'
>>> 
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> str1[0]
'h'
>>> str1[0] = "a"
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    str1[0] = "a"
TypeError: 'str' object does not support item assignment
>>> del str1[0]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    del str1[0]
TypeError: 'str' object doesn't support item deletion
>>> 
>>> dict.__doc__
"dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
>>> print(dict.__doc__)
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> help(str.capitalize)
Help on method_descriptor:

capitalize(self, /)
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> str.capitalize
Help on method_descriptor in str:

str.capitalize = capitalize(self, /)
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

help> str.lower
Help on method_descriptor in str:

str.lower = lower(self, /)
    Return a copy of the string converted to lowercase.

help> str.upper
Help on method_descriptor in str:

str.upper = upper(self, /)
    Return a copy of the string converted to uppercase.

help> quit()
No Python documentation found for 'quit()'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> 
>>> dict(str)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    dict(str)
TypeError: 'type' object is not iterable
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1.capitalize()
'Hello this is python programming'
>>> str1
'hellO this is Python PROgramming'
>>> str1.casefold()
'hello this is python programming'
>>> str1.lower()
'hello this is python programming'
>>> str1.center()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    str1.center()
TypeError: center() takes at least 1 argument (0 given)
>>> help(str1.center)
Help on built-in function center:

center(width, fillchar=' ', /) method of builtins.str instance
    Return a centered string of length width.
    
    Padding is done using the specified fill character (default is a space).

>>> str1.center(100)
'                                  hellO this is Python PROgramming                                  '
>>> str1.center(150)
'                                                           hellO this is Python PROgramming                                                           '
>>> str1.center(130)
'                                                 hellO this is Python PROgramming                                                 '
>>> str1.center(130, *)
SyntaxError: invalid syntax
>>> str1.center(130, "*")
'*************************************************hellO this is Python PROgramming*************************************************'
>>> str1.center(115, "*")
'******************************************hellO this is Python PROgramming*****************************************'
>>> str1.center(110, "*")
'***************************************hellO this is Python PROgramming***************************************'
>>> str1.count('p')
0
>>> str1.count('P')
2
>>> str1.count('Python')
1
>>> str1.endswith("g")
True
>>> str1.endswith("mming")
True
>>> str1.endswith("mminG")
False
>>> str1.startswith("mminG")
False
>>> str1.startswith("hell")
True
>>> str1.find('P')
14
>>> str1.index('P')
14
>>> str1.find('x')
-1
>>> str1.index('x')
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    str1.index('x')
ValueError: substring not found
>>> str1.rfind('x')
-1
>>> str1.rfind('P')
21
>>> str1[14]
'P'
>>> str1[21]
'P'
>>> str1.find('i')
8
>>> str1.rfind('i')
29
>>> str1.find('i', 9)
11
>>> str1.find('i', 12)
29
>>> str1.isalnum()
False
>>> "hello".isalnum()
True
>>> str1.replace("i", "x")
'hellO thxs xs Python PROgrammxng'
>>> str1.replace(" ", "")
'hellOthisisPythonPROgramming'
>>> str2 = str1.replace(" ", "")
>>> str2.isalnum()
True
>>> str1.replace(" ", "").isalnum()
True
>>> str1.replace("Python", "Java")
'hellO this is Java PROgramming'
>>> str1
'hellO this is Python PROgramming'
>>> str1.title()
'Hello This Is Python Programming'
>>> str1.istitle()
False
>>> 123 = 34
SyntaxError: can't assign to literal
>>> "123".isidentifier()
False
>>> "a123".isidentifier()
True
>>> "     hello world     ".strip()
'hello world'
>>> "     hello world     ".strip(chars='h')
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    "     hello world     ".strip(chars='h')
TypeError: strip() takes no keyword arguments
>>> "     hello world     ".strip('h')
'     hello world     '
>>> "hello world     h".strip('h')
'ello world     '
>>> "hello world     h".strip('hello')
' world     '
>>> 
