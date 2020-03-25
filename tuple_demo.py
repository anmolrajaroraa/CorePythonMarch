Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list and tuple can store any type of data
>>> #array stores only one type of data
>>> #array is mutable but has fixed size
>>> #tuple is not mutable and has fixed size also
>>> tuple1 = (1,2,3,4,5)
>>> tuple1
(1, 2, 3, 4, 5)
>>> type(tuple1)
<class 'tuple'>
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> tuple1.count(5)
1
>>> tuple1.index(5)
4
>>> tuple1 = (1,2,3,4,5,"text",True,10.2,0xabc)
>>> tuple1
(1, 2, 3, 4, 5, 'text', True, 10.2, 2748)
>>> tuple1[0]
1
>>> tuple1[3]
4
>>> tuple1[5]
'text'
>>> tuple1[-1]
2748
>>> tuple1[:5]
(1, 2, 3, 4, 5)
>>> tuple1[5:]
('text', True, 10.2, 2748)
>>> 

Task
Login and register application
users = [
["ram@gmail.com", "ram123", "Ram Kumar"],
[],
[]
    ]
