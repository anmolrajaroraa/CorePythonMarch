Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> #list and tuple can store any type of data
>>> #array stores only one type of data
>>> #array is mutable but has fixed size
>>> #list is also mutable and has flexible size also
SyntaxError: invalid syntax
>>> list1 = [ 1, 2, 3, 4, 5, "text", True, 10.2, 0xabc ]
>>> list1[0]
1
>>> list1[-1]
2748
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> hex(list1[-1])
'0xabc'
>>> list1 = [ 1, 2, 3, 4, 5, "text", True, 10.2, 0xabc, (1,2,3), [4,5,6] ]
>>> list1[-1]
[4, 5, 6]
>>> list1[-2]
(1, 2, 3)
>>> list1 = [ 1, 2, 3, 4, 5, "text", True, 10.2, 0xabc, (1,2,3), [4,5,6], [ [1,2,3], [4,5,6], [7,8,9,0] ] ]
>>> list1[-1]
[[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]]
>>> list1[-1][0][2]
3
>>> list1[-1][0][0]
1
>>> list1[5]
'text'
>>> list1[5][0]
't'
>>> list1[-2][0]
4
>>> list1[-1][0][2]
3
>>> list1.append(1000)
>>> list1
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6], [[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]], 1000]
>>> list1 = None
>>> list1
>>> list1 = [ 1, 2, 3, 4, 5, "text", True, 10.2, 0xabc, (1,2,3), [4,5,6], [ [1,2,3], [4,5,6], [7,8,9,0] ] ]
>>> list1.clear()
>>> list1
[]
>>> list1 = [ 1, 2, 3, 4, 5, "text", True, 10.2, 0xabc, (1,2,3), [4,5,6] ]
>>> list2 = list1
>>> list1
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6]]
>>> list2
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6]]
>>> list3 = list1.copy()
>>> list3
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6]]
>>> id(list1) == id(list2)
True
>>> id(list1) == id(list3)
False
>>> list1.append(2000)
>>> list2
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6], 2000]
>>> list3
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6]]
>>> list1[-2]
[4, 5, 6]
>>> list1[-2].append(7)
>>> list1
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7], 2000]
>>> list2
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7], 2000]
>>> list3
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7]]
>>> #list1 = [ 1, 2, 3, 4, 5, "text", True, 10.2, 0xabc, &23, &45 ]
>>> #list3 = [ 1, 2, 3, 4, 5, "text", True, 10.2, 0xabc, &23, &45 ]
>>> import copy
>>> list4 = copy.deepcopy(list1)
>>> list1
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7], 2000]
>>> list4
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7], 2000]
>>> list3
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7]]
>>> list1[-2].append(8)
>>> list1
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7, 8], 2000]
>>> list3
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7, 8]]
>>> list4
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7], 2000]
>>> list1.count(1)
2
>>> list1.count(2)
1
>>> list1.count(4)
1
>>> list1.count((1,2,3))
1
>>> list1.count(0)
0
>>> list1 = [1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7, 8], 2000, False]
>>> list1.count(0)
1
>>> list1.append(300)
>>> list1.extend(300)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    list1.extend(300)
TypeError: 'int' object is not iterable
>>> list1.append( [100,200,300] )
>>> list1.extend( [100,200,300] )
>>> list1
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7, 8], 2000, False, 300, [100, 200, 300], 100, 200, 300]
>>> #list1.append( "python" )
>>> #list1.extend( "python" )
>>> #append adds the element provided to it as it is without checking for the type
>>> #extend uses an iterable to fetch elements one by one from new list and insert into the old list
>>> list1.append( "python" )
>>> list1.extend( "python" )
>>> list1
[1, 2, 3, 4, 5, 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7, 8], 2000, False, 300, [100, 200, 300], 100, 200, 300, 'python', 'p', 'y', 't', 'h', 'o', 'n']
>>> list1.index(1)
0
>>> list1.index(1, 1)
6
>>> list1.index(1, 7)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    list1.index(1, 7)
ValueError: 1 is not in list
>>> list1.insert(5, "new object")
>>> list1
[1, 2, 3, 4, 5, 'new object', 'text', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7, 8], 2000, False, 300, [100, 200, 300], 100, 200, 300, 'python', 'p', 'y', 't', 'h', 'o', 'n']
>>> list1[6] = "Ram"
>>> list1
[1, 2, 3, 4, 5, 'new object', 'Ram', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7, 8], 2000, False, 300, [100, 200, 300], 100, 200, 300, 'python', 'p', 'y', 't', 'h', 'o', 'n']
>>> del list1[6]
>>> list1
[1, 2, 3, 4, 5, 'new object', True, 10.2, 2748, (1, 2, 3), [4, 5, 6, 7, 8], 2000, False, 300, [100, 200, 300], 100, 200, 300, 'python', 'p', 'y', 't', 'h', 'o', 'n']
>>> list1[11][:3]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    list1[11][:3]
TypeError: 'int' object is not subscriptable
>>> list1[10][:3]
[4, 5, 6]
>>> 
