Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> [1,2,3,4,5,6]
[1, 2, 3, 4, 5, 6]
>>> (1,2,3,4,5,6)
(1, 2, 3, 4, 5, 6)
>>> {"name" : "Ram"}
{'name': 'Ram'}
>>> {"name" : "Ram", "name" : "Shyam"}
{'name': 'Shyam'}
>>> {1,2,3,4,5}
{1, 2, 3, 4, 5}
>>> set1 = {1,2,3,4,5}
>>> set1[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set1[0]
TypeError: 'set' object is not subscriptable
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> set1.add(6)
>>> set1
{1, 2, 3, 4, 5, 6}
>>> set1.add(6)
>>> set1
{1, 2, 3, 4, 5, 6}
>>> set1 = {1,2,3,4,5,6,6}
>>> set1
{1, 2, 3, 4, 5, 6}
>>> set1 = {1,2,3,4,5,6,6,True}
>>> set1
{1, 2, 3, 4, 5, 6}
>>> set1 = {2,3,4,5,6,6,True}
>>> set1
{True, 2, 3, 4, 5, 6}
>>> set1 = {2,3,4,5,6,6,True,1}
>>> 
>>> set1
{True, 2, 3, 4, 5, 6}
>>> set1 = {2,3,4,5,6,6,True,1,0,False}
>>> set1
{0, True, 2, 3, 4, 5, 6}
>>> #hashing algorithm
>>> set1 = {2,3,4,5,6,6,True,1, "Ram", "Shyam", "Mohan", "Jenny", "Anna"}
>>> set1
{True, 2, 3, 4, 5, 6, 'Ram', 'Shyam', 'Anna', 'Jenny', 'Mohan'}
>>> set1 = {2,3,4,5,6,6,True,1, "Ram", "Shyam", "Mohan", "Jenny", "Anna", 100, 9930, 34, 34333}
>>> set1
{True, 2, 3, 4, 5, 6, 'Ram', 100, 34, 9930, 'Shyam', 'Anna', 'Jenny', 34333, 'Mohan'}
>>> set1[0]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    set1[0]
TypeError: 'set' object is not subscriptable
>>> for element in set1:
	print(element)

	
True
2
3
4
5
6
Ram
100
34
9930
Shyam
Anna
Jenny
34333
Mohan
>>> set1 = {2,3,4,5,6,6,True,1, "Ram", "Shyam", "Mohan", "Jenny", "Anna", 100, 9930, 34, 34333, 123}
>>> for element in set1:
	print(element)

	
True
2
3
4
5
6
Ram
100
34
9930
Shyam
Anna
Jenny
123
34333
Mohan
>>> # set keeps only the unique values
>>> # set works on the first come first served basis
>>> # set uses hashing algorithm to store elements (randomly)
>>> set1.remove(123)
>>> set1
{True, 2, 3, 4, 5, 6, 'Ram', 100, 34, 9930, 'Shyam', 'Anna', 'Jenny', 34333, 'Mohan'}
>>> type(set1)
<class 'set'>
>>> frozenset(set)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    frozenset(set)
TypeError: 'type' object is not iterable
>>> frozenset(set1)
frozenset({True, 2, 3, 4, 5, 6, 'Ram', 100, 34, 9930, 'Shyam', 'Anna', 'Jenny', 34333, 'Mohan'})
>>> fset = frozenset(set1)
>>> type(fset)
<class 'frozenset'>
>>> dir(set1)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> dir(fset)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> set2 = frozenset({1,2,3,4,5})
>>> x = {}
>>> type(x)
<class 'dict'>
>>> x = set()
>>> x
set()
>>> x.add(10)
>>> x
{10}
>>> x = {}
>>> x.add(10)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    x.add(10)
AttributeError: 'dict' object has no attribute 'add'
>>> x
{}
>>> set1 = {2,3,4,5,6,6,True,1, "Ram", "Shyam", "Mohan", "Jenny", "Anna", 100, 9930, 34, 34333, 123}
>>> set2 = {"Jenny", "Anna", 100, 9930, 34, 34333, 123}
>>> set1 - set2
{True, 2, 3, 4, 5, 6, 'Ram', 'Shyam', 'Mohan'}
>>> set1.difference(set2)
{True, 2, 3, 4, 5, 6, 'Ram', 'Shyam', 'Mohan'}
>>> set1.difference_update(set2)
>>> set1
{True, 2, 3, 4, 5, 6, 'Ram', 'Shyam', 'Mohan'}
>>> set1 = {2,3,4,5,6,6,True,1, "Ram", "Shyam", "Mohan", "Jenny", "Anna", 100, 9930, 34, 34333, 123}
>>> set1.difference(set2)
{True, 2, 3, 4, 5, 6, 'Ram', 'Shyam', 'Mohan'}
>>> set1
{True, 2, 3, 4, 5, 6, 'Ram', 100, 34, 9930, 'Shyam', 'Anna', 'Jenny', 123, 34333, 'Mohan'}
>>> set1.discard(10)
>>> set1.remove(10)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    set1.remove(10)
KeyError: 10
>>> set1.discard(100)
>>> set1
{True, 2, 3, 4, 5, 6, 'Ram', 34, 9930, 'Shyam', 'Anna', 'Jenny', 123, 34333, 'Mohan'}
>>> set1.discard(100)
>>> set1.intersection(set2)
{34, 9930, 'Anna', 'Jenny', 123, 34333}
>>> set1.union(set2)
{True, 2, 3, 4, 5, 6, 9930, 'Jenny', 34333, 34, 'Ram', 100, 'Shyam', 'Anna', 123, 'Mohan'}
>>> set1.isdisjoint(set2)
False
>>> set3 = {999,888,777}
>>> set1.isdisjoint(set3)
True
>>> set1.issuperset(set2)
False
>>> set1.add(100)
>>> set1.issuperset(set2)
True
>>> set1
{True, 2, 3, 4, 5, 6, 'Ram', 100, 34, 9930, 'Shyam', 'Anna', 'Jenny', 123, 34333, 'Mohan'}
>>> set2
{34, 100, 9930, 'Anna', 'Jenny', 123, 34333}
>>> set2.issubset(set1)
True
>>> set1.pop()
True
>>> set1.pop()
2
>>> set1.pop()
3
>>> set1.pop()
4
>>> 
>>> set1.pop()
5
>>> set1.pop()
6
>>> set1.pop()
'Ram'
>>> set1.update(set3)
>>> set1
{34, 100, 999, 777, 9930, 'Shyam', 'Anna', 'Jenny', 888, 123, 34333, 'Mohan'}
>>> 