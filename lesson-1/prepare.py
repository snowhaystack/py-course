import numpy as np
import warnings
warnings.filterwarnings('ignore')
ARRAY_INT = range(2,10)
##FUNCTION SECTION
def endTest(cursor):
    ####### START ########
    cursor += 1
    print(f'{"END ------> "}{cursor}')
    print('')
    return cursor
    ###### END ##########
def startTest(cursor,desc):
    ####### START ########
    cursor += 1
    print(f'START ------> {cursor} {desc} ')
    ###### END ##########
#pass, and _ for sintax
#else if => elif
#case switch from 3.10+
cursor = 0
##########################
desc = 'array'
startTest(cursor ,desc)
a = np.array([1,2,3,4])
test = 'halo'
print(test[3])
cursor = endTest(cursor)
##########################
desc = 'for range'
startTest(cursor,desc)
for b in range(a.size):
    if b % 2 == 0:
        continue
    else:
        print(b)
        #pass
cursor = endTest(cursor)
##########################
startTest(cursor,'for constants')
for b in ARRAY_INT:
    if b % 2 != 0:
        continue
    else:
        print(b)
        #pass
cursor = endTest(cursor)
##########################
startTest(cursor,'callable')
#if object is callable
print(callable(str.split))
#if object has this attribute
print(hasattr(str,'title'))
#string formatted as utf8
for e in dir(str):
    pass
    #print(e, end = '-> ')
    #print(callable(str[e])) ##dosen't work callable variable
cursor = endTest(cursor)
##########################
startTest(cursor,'slicing')
#slicing
testo = "nel mezzo del cammin di nostra vita"
print(testo[2:])
print(testo[:8])
print(testo[::2])
print(testo[::-1])
for i in range(len(testo)):
    #print(testo[i * -1],end="")
    pass
cursor = endTest(cursor)
##########################
startTest(cursor,'string')
#ljust(50)
print(testo.ljust(50))
print(testo.rjust(50))
cursor = endTest(cursor)
##########################
startTest(cursor,'formatting')
print('{1} {0}'.format('one','two'))
print('{:4f}'.format(10.2))
print(f'{testo.upper():<10} world')
c = "{uno}, -- {due}"  .format(uno=1, due='aaaa')
print(c)
print(str(cursor))
cursor = endTest(cursor)
##########################
startTest(cursor,'map string')
trans = str.maketrans('abc','bnm')
trans_back = str.maketrans('bnm','abc')
string = "anwer bsc"
codify = string.translate(trans)
read = string.translate(trans_back)
print(codify)
print(read)
cursor = endTest(cursor)
