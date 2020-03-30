Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> employee = {
	name : "Abcd"
	}
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    name : "Abcd"
NameError: name 'name' is not defined
>>> employee = {
	id : "Abcd"
	}
>>> employee["id"]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    employee["id"]
KeyError: 'id'
>>> employee[id]
'Abcd'
>>> id(employee)
4483768256
>>> employee = {
	"e_id" : 101,
	"name" : "Ram Kumar",
	"salary" : 25000,
	"contact" : [1234, 5678],
	"addresses" : {
		"home" : "Rohini",
		"office" : "NSP"
		}
	}
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 
>>> help(dict.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.

>>> list_of_employee_keys = employee.keys()
>>> list_of_employee_key
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list_of_employee_key
NameError: name 'list_of_employee_key' is not defined
>>> list_of_employee_keys
dict_keys(['e_id', 'name', 'salary', 'contact', 'addresses'])
>>> 
>>> #static method
>>> dict.fromkeys(list_of_employee_keys)
{'e_id': None, 'name': None, 'salary': None, 'contact': None, 'addresses': None}
>>> new_employee = dict.fromkeys(list_of_employee_keys)
>>> new_employee
{'e_id': None, 'name': None, 'salary': None, 'contact': None, 'addresses': None}
>>> new_employee = dict.fromkeys(list_of_employee_keys, "no data")
>>> new_employee
{'e_id': 'no data', 'name': 'no data', 'salary': 'no data', 'contact': 'no data', 'addresses': 'no data'}
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
 |  __reversed__(self, /)
 |      Return a reverse iterator over the dict keys.
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
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |      
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.
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

>>> new_employee.pop()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    new_employee.pop()
TypeError: pop expected at least 1 argument, got 0
>>> new_employee.popitem()
('addresses', 'no data')
>>> new_employee.popitem('salary')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    new_employee.popitem('salary')
TypeError: popitem() takes no arguments (1 given)
>>> new_employee.pop('salary')
'no data'
>>> new_employee
{'e_id': 'no data', 'name': 'no data', 'contact': 'no data'}
>>> new_employee.pop('salary')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    new_employee.pop('salary')
KeyError: 'salary'
>>> new_employee.pop('salary', 'key not found')
'key not found'
>>> new_employee.pop('e_id', 'key not found')
'no data'
>>> new_employee.pop('e_id', 'key not found')
'key not found'
>>> new_employee = dict.fromkeys(list_of_employee_keys, "no data")
>>> new_employee
{'e_id': 'no data', 'name': 'no data', 'salary': 'no data', 'contact': 'no data', 'addresses': 'no data'}
>>> new_employee["salary"] = 0
>>> new_employee
{'e_id': 'no data', 'name': 'no data', 'salary': 0, 'contact': 'no data', 'addresses': 'no data'}
>>> new_employee["salary"] = 100000
>>> new_employee["salary"] = 0
>>> new_employee
{'e_id': 'no data', 'name': 'no data', 'salary': 0, 'contact': 'no data', 'addresses': 'no data'}
>>> del new_employee['salary']
>>> new_employee
{'e_id': 'no data', 'name': 'no data', 'contact': 'no data', 'addresses': 'no data'}
>>> new_employee.setdeafault('salary', 0)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    new_employee.setdeafault('salary', 0)
AttributeError: 'dict' object has no attribute 'setdeafault'
>>> new_employee.setdefault('salary', 0)
0
>>> new_employee
{'e_id': 'no data', 'name': 'no data', 'contact': 'no data', 'addresses': 'no data', 'salary': 0}
>>> new_employee["salary"] = 100000
>>> new_employee
{'e_id': 'no data', 'name': 'no data', 'contact': 'no data', 'addresses': 'no data', 'salary': 100000}
>>> new_employee.setdefault('salary', 0)
100000
>>> job_profile = {
	"designation" : "developer",
	"department" : "IT",
	"team" : "Alpha"
	}
>>> new_employee.update(job_profile)
>>> new_employee
{'e_id': 'no data', 'name': 'no data', 'contact': 'no data', 'addresses': 'no data', 'salary': 100000, 'designation': 'developer', 'department': 'IT', 'team': 'Alpha'}
>>> 
>>> 
>>> print("Designation is {}, department is {}, team is {}".format(designation, department, team))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print("Designation is {}, department is {}, team is {}".format(designation, department, team))
NameError: name 'designation' is not defined
>>> print("Designation is {}, department is {}, team is {}".format(job_profile))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print("Designation is {}, department is {}, team is {}".format(job_profile))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("Designation is {}, department is {}, team is {}".format_map(job_profile))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print("Designation is {}, department is {}, team is {}".format_map(job_profile))
ValueError: Format string contains positional fields
>>> print("Designation is {designation}, department is {department}, team is {team}".format_map(job_profile))
Designation is developer, department is IT, team is Alpha
>>> 