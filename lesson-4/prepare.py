##VARIABLE INIT
cursor = 0
desc = 'section'
##FUNCTION SECTION
def endTest():
    ####### START ########
    global cursor
    logger.info(f'{"END ------> "}{cursor}')
    logger.info('')
    return cursor
    ###### END ##########
def startTest(desc):
    ####### START ########
    global cursor
    cursor += 1
    logger.info(f'START ------> {cursor} {desc} ')
    ###### END ##########
##USAGE XAMPLE
##########################
import logging,random
logger = logging.getLogger("&8&")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
#handler = logging.FileHandler("log-2023-01-10.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


startTest('Lambda')
data = [{'first':'yy','last':'xx'},{'first':'ii','last':'pp'},{'first':'ss','last':'zz'}]
data1 = [{'first':5,'last':'xx'},{'first':3,'last':'pp'},{'first':1,'last':'zz'}]
datal = sorted(data,key=lambda item: item['first']) #sort all dictionary on item['first'] element
datal1 = sorted(data1,key=lambda item: item['first'])
print(datal)
print(datal1)
double = lambda x : x*2
pow = lambda item : item*item

def apply_calc(calc, value): #level up function
    result = calc(value)
    return result

print(apply_calc(double, 10))
print(apply_calc(pow, 10))
print(apply_calc(lambda xx: xx*xx+xx, 100)) # 100*100+100

l3 = [89,33,11,"77",44]
#lsorted2 = sorted(l3) #error, not all items have same type
lsorted2 = sorted(l3, key=lambda x: int(x))
print(lsorted2)


l3 = [89,33,11,"77",44]
#lsorted2 = sorted(l3) #error, not all items have same type
lsorted2 = sorted(l3, key=lambda x: int(x))
#fomat error
try:
    l3 = [89,33,11,"77",44]
    lsorted2 = sorted(l3)
    logger.info(lsorted2)
except Exception as e:
    logger.error(e)
#zero division exception
try:
    a=1/0
except ZeroDivisionError as e:
    logger.critical("0 division error!!!")
#regular execution
try:
    l3 = [89,33,11,77,44]
    lsorted2 = sorted(l3)
    logger.info(lsorted2)
except Exception as e:
    logger.error(e)
else:
    logger.info("Nessun Errore")
finally:
    logger.info("finally block exec")
    ##############################
print(lsorted2)
cursor = endTest()

##########################
startTest('variable')
my_var = "GLOBAL"

def f1():
    my_var = "LOCAL F1"
    print(my_var)

def f2():
    my_var = "LOCAL F2"
    print(my_var)
    f1()
    print(my_var)

def f3():
    f2()
    global my_var
    my_var = "LOCAL F3 over GLOBAL"
    print(my_var)

def f4():
    def ff4():
        print(my_var)
    ff4()
   

print(my_var)
f3()
print(my_var)
f4()

cursor = endTest()

##########################
startTest('iteration')
#PEP-0234
L = [2,3,4,5]
for i,val in enumerate(L):
    print(i,val)
R = [6,7,9,8]
print(hasattr(L,'__iter__'))
l1 = [0,0,0,0]
print(all(l1))
l2 = [1,'hello',10,(1,2)]
print(all(l2))
l2.append(0)
print(all(l2))
print(any(l1))
print(any(l2))
l3 = [1,2,3,10,8000]
print(max(l3)) #only same type
print(min(l3)) #only same type
l3.append('10000')
#print(max(l3)) #error, int and string type
#print(min(l3)) #error, int and string type
print(max(l3,key=lambda item: int(item)))
print(min(l3,key=lambda item: int(item)))
for i,item in enumerate(l3):
    print(i,item,type(item),sep='->')
l1[3] = 'HHHHH'
for x,y in zip(l1,l2):
    print(x,y,sep="-")
l1.append('UUUU')
for x,y in zip(l1,l2):
    print(x,y,sep="-")#UUU not printed beacuse is out of range

from itertools import * #import permutation
p = permutations(l1)
print(p)
print(*p)#for cycle with print(p)
print('-')
print(*p)#empty print, memory cleared
print('-')
ll = [10,20,30]
p = permutations(ll)
print(*p)
c= combinations(ll,2)
print(*c)
c= combinations(ll,3)
print(*c)
c= combinations(ll,1)
print(*c)
p = product(l1,l2)
print(*p)
cursor = endTest()
##END USAGE EXAMPLE
##########################
startTest('list comprehensions')
#for without for
l1 = [n ** 2 for n in range(12) ]
print(l1)
l1 = [n*2 for n in range(100)]
print(l1)
l1 = [n*2 for n in range(100) if n%2==0 or n==1]
print(l1)
l2 = [(n,m) for n in range(10) for m in range(20)]
print(l2)
deck = [(seed,value) 
            for seed in ['bastoni', 'coppe', 'spade', 'denari'] 
                for value in ['Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Fante', 'Cavallo', 'Re']]
print('deck')
print(deck)
deck_value = {item:i for i,item in enumerate(deck)}
print('deck value')
print(deck_value)
#enumerate count all items with index
full_deck = {item:i for i,item in enumerate([(seed,value) 
            for seed in ['bastoni', 'coppe', 'spade', 'denari'] 
                for value in ['Asso', 'Due', 'Tre', 'Quattro', 'Cinque', 'Sei', 'Sette', 'Fante', 'Cavallo', 'Re']])}
print(f'full deck ->{full_deck}')
card = full_deck[random.choice(list(full_deck.keys()))]
print(f'card index->{card}')
card = random.choice(list(full_deck.keys()))
print(f'card value->{card}')
card = full_deck.popitem()
print(f'card->{card}')

cursor = endTest()
##########################
startTest('generator')
def gen():
    for n in range(12):
        yield n**2
G = gen()
print(G)
cursor = endTest()
##########################
startTest('functional programming')
square = lambda x: x ** 2
for val in map(square, range(10)):
    print(val, end='-')

def calculator(operator, value):
    if callable(operator):
        return operator(value)
    else: 
        return f'{operator} => {value}'
def power(value):
    return value**2
def double(value):
    return value*2

print(calculator(power,10))
print(calculator(double,10))


l1 = [10,20,30,40]
l2 = map(power,l1)
print(l2)
l3 = map(lambda x: x*x+100, l1)
print(*l3)
l4 = ['xxx','yyy','zzz','test']
print(*map(lambda val: val.upper() if 'test' in val else 'N/A', l4))

from functools import reduce
def sum(a,b):
    return a+b
l5 = reduce(sum,l1)
print(l5) # => 10,20,30,40,60,100 
def option(or_txt, add_txt):
    return or_txt + '<select>' + str(add_txt) + '</select>'
option_html = str(reduce(option,l1,'<option>')) + '</option>'

#py syntax
option_html = f"{reduce(lambda select,option: f'{select}<option>{str(option)}</option>',l1,'</select>')}</select>"

def option_build(list):
    return f"{reduce(lambda select,option: f'{select}<option>{str(option)}</option>',list,'</select>')}</select>"


cursor = endTest()