##VARIABLE INIT
cursor = 0
desc = 'section'
##FUNCTION SECTION
def endTest():
    ####### START ########
    global cursor
    print(f'{"END ------> "}{cursor}')
    print('')
    return cursor
    ###### END ##########
def startTest(desc):
    ####### START ########
    global cursor
    cursor += 1
    print(f'START ------> {cursor} {desc} ')
    ###### END ##########
##########################
desc = 'list'
startTest(desc)
'''
list definition =>  [] === False
list => keyword
in operator -> True|False
matrix => multidimensional list, list position == matrixx row
'''
list = []
print(type(list))
print(dir(list))
list = [1,"two",(3,4),[5,"six"]]
print(list.index("two"))
list.remove("two")
print(list)
print(list[2])
print(list[0:2])
print(list[-1])
print(list.reverse())
print(list[-1])
list.pop()
list.append(5)
list.append([1,2,3,4,5])
print(list)
list.insert(3,('u','v'))
print(list)
list1 = [100,200]
list.extend(list1)
print(list)
list2 = list + [900,88]
print(list2)
list3 = [1,2]
list4 = list3 * 10
print(list4)
list5 = [1,2,3]
a,b,c = list5
print(a)
#unpacking
list2[0] = 'tia'
list2[-1] = 'snow'
print(list2)
a,*_,b = list2 #a firts element, b last element, *_ other elements
a,*c,b = list2
print(c)
list2.append(100)
print(list2.count(100))
list2.clear()
print(list2)
for item in list1:
    print(f'=> {item}')
cursor = endTest()
##########################
desc = 'touple'
'''
touple definition => ()
elements touple can't be modified! => only element info
element could be repeated
'''
startTest(desc)
t = ()
print(type(t))
print(dir(t))
print(t.__len__())
#t[1]='test' #NOT WORKING, CAN'T ASSIGN VALUE TO TOUPLE
cursor = endTest()

##########################
desc = 'dictionary'
'''
dictionary definition => { key:val }
serach => key and not index
slicing dosen't work
useful with json
get methond for extract val from dictionary
get key not found => none [ not exception ]
method => [ keys(), values(), items()] all method {iterable}
keys() => list of all key
values() => list with all value 
items() => touple list { key:val }
update() => update val from key, if key dosen't exist update will add key:val
* => unpacking iterable values
** => unpacking dictionary [concat dictionary and modify value from same key]
'''
startTest(desc)
d = {}
print(type(d))
print(dir(d))
d['one'] = 100
print(d)
print(d['one'])
#print(d['two']) #error
print(d.get('two'))
print(100 in d)
print('one' in d)
d[2] = 'test'
d[(1,2)] = [1,2,3,4]
print(d)
print(d.pop(2)) #delete this element
print(d)
d.pop(3,'N/A') #N/A default value, if element not found return N/A and not error
d.pop(3,None) #None default value, if element not found return None and not error
d.popitem()
print(d)
d[90] = 'test1'
d['t'] = [1,2,3,4,5]
print(d)
print(d.get('t'))
print(d.get('t1'))
print(d.get('t1','N/A'))
print(d.setdefault('t1','N/A')) #setdefault return N/A but add element into dictionary
print(d)
print(d.items()) #touple list (key:val)
print(d.keys())
print(d.values())
for k,v in d.items():
    print(f'key => {k} : val => {v}')
user = {'name':'tia','username':'snow','birth':1996}
print("{name}, {username} => birth year {birth}".format(**user))
print(id(d))
d1 = d
print(id(d1))
d1['uu'] = 'jj'
print(d)
print(d1)
d2 = d.copy()
d[1000] = 100
print(d)
print(d1)
print(d2)
cursor = endTest()

##########################
desc = 'sets'
'''
sets definition => { val1,val2 }
object into set can't be modified!
add|remove data
unique condition!
'''
startTest(desc)
s = {100}
print(type(s))
print(dir(s))
s.add(200)
print(s)
s.add(100)
print(s) #100 already into set, not added
s1 = {100,200,300}
s2 = {100,400,500}
s2.add(600)
#difference
print(s1.difference(s2))
print(s1)
print(s1.difference_update(s2))
print(s1.intersection(s2))
s1.add(100)
print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1)
print(s2)
print(s1.isdisjoint(s2))
print(s1.intersection_update(s2))
print(s1)
print(s2)
s3 = {600,500}
print(s3.issubset(s2))#true, s2 contain s3 elements
print(s3.issuperset(s2))#false
print(s2.issuperset(s3))#false
s2.pop() #delete random element
print(s2)
print(s1.update(s3))
print(s1)
print(s3)
print(s1.symmetric_difference(s3))#element not in both sets

cursor = endTest()
##########################
desc = 'abs'
startTest(desc)
cursor = endTest()

##########################
##########################
desc = 'iterable => all'
startTest(desc)
print(all([1,True]))
print(all([1,True,()]))
print(all([1,True,(11)]))
print(all([1,True,[]]))
print(all([1,True,[18]]))
print(all([1,True,{}]))
print(all([1,True,{'x':18}]))
cursor = endTest()

##########################
##########################
desc = 'iterable => any'
startTest(desc)
print(any([1,True]))
print(any([1,True,()]))
print(max([1,20,100,100,999]))
cursor = endTest()

##########################
##########################
desc = 'chr(i) <=> ord()'
startTest(desc)
cursor = endTest()

##########################
##########################
desc = 'dir(object)'
startTest(desc)
cursor = endTest()

##########################
##########################
desc = 'len(object)'
startTest(desc)
print(len([1,20,100,100,999]))
cursor = endTest()

##########################
##########################
desc = 'vars(object)'
startTest(desc)
print(vars())
cursor = endTest()

##########################
##########################
desc = 'eval(expr [,globals [, locals]])'
startTest(desc)
print(eval('2 + 2'))
expr = "10 *2 + 1 + 900"
print(eval(expr))
cursor = endTest()

##########################
##########################
desc = 'exec(code [,globals [, locals]])'
startTest(desc)
exec("test=eval('10+10')")
print(test)
cursor = endTest()

##########################
##########################
desc = 'print'
startTest(desc)
print("xxx","yyyy")
print("xxx","yyyy",sep="*")
print("xxx","yyyy",sep="*",end="-->EOF")
cursor = endTest()

##########################
##########################
desc = 'import'
startTest(desc)
'''
import math
dir(math)
math.sin(10)
------------
from math import * 
can use sin(10) without math #debugging problem!!
'''
cursor = endTest()

##########################