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
def p(x):
    ####### START ########
    print(f'{x}')
    ###### END ##########
##USAGE XAMPLE
##########################
import datetime,shelve,logging,random

startTest('time')
d1 = datetime.datetime.now()
p(d1)
#import datetime from datetime ( use datetime.now() and not datetime.datetime.now())
#add 1000 days to current date
thousanDays = datetime.timedelta(days=1000)
dt_thousand = d1 + thousanDays
p(dt_thousand)
#p(strftime(dt_thousand))
p(dir(datetime))
d3 = datetime.date(2023,4,3)
p(d3)
p(d3.day)
p(d3.year)
p(d3.month)
p(type(d3))
t1 = datetime.time(12,3,8)
p(t1.hour)
p(t1.minute)
p(t1.second)
d4 = datetime.datetime(2023,1,5,11,45,5)
p(d4)
threedays = datetime.timedelta(days=3)
d5 = d4 + threedays
p(d5)
p(d5.timestamp()) #from january 1970 in secs
d10 = datetime.date.fromtimestamp(167285000)
p(d10)
p(d10.strftime('Year: %Y, month: %B, day: %d'))
sd1 = 'Year: 1975, month: April, day: 21'
sd2 = 'Year: 2023, month: April, day: 21'
#Year: %Y, month: %B, day: %d => decode key
dd1 = datetime.datetime.strptime(sd1,'Year: %Y, month: %B, day: %d')
p(dd1)
cursor = endTest()

##########################
startTest('shelf module')
'''
#create new files in this directory [ .bak, .dat, .dir]
shelf = shelve.open('variable-tia')
shelf['first_name'] = 'yy'
shelf['last_name'] = 'xx'

#if line 65 and 66 are commented these 2 variable
#will be catched by filesystem
first_name = shelf['first_name']
last_name = shelf['last_name'] 

shelf.close()
'''
cursor = endTest()

##########################
startTest('log method, logging module')
#DEGUB,INFO,WARNING,ERROR,CRITICAL
#logging.getLogger(__name__)
#if(__name__ == "__main__" )
logger = logging.getLogger(__name__)
#logger = logging.getLogger("Py course") => name == Py course
#--------------------
#init log definition
logger.setLevel(logging.DEBUG) #set level of print loggin [ default is warning ]
handler = logging.StreamHandler() #define printer into console
#handler = logging.FileHandler("log-2023-01-10.log") #define printer into file log-2023-01-10.log
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
#--------------------
logger.info('Info Log') #no print
logger.debug('Debug Log') #print ok
logger.warning('Warning Log') #print ok
logger.error('Error Log') #print ok
logger.critical('Critical Log') #print ok
cursor = endTest()
##########################
startTest('random')
p(random.random())
random.seed(100)
p(random.randint(1,1000))
l1 = ["hello","word",1,2,3]
p(random.choice(l1))
p(random.choice(l1))
#p(random.choice(l1,3))
p(random.shuffle(l1))
cursor = endTest()
##########################
startTest('functions')
#def foo(p1,p2="default",*p3)
#*p3 will receive third param and all other params after third
def my_func(p1, p2, p3=0):
    p(f"p1->{p1}")
    p(f"p2->{p2}")
    p(f"p3->{p3}")
    p('-------')

def my_func2(p1, p2, p3="valore default"):
    p(f"p1->{p1}")
    p(f"p2->{p2}")
    p(f"p3->{p3}")
    p('-------')

def my_func3(p1, *p2):
    p(f"p1->{p1}")
    p(f"p2->{p2}")
    p('-------')
    return 'XX'

my_func(1,"hello")
my_func(p2="world",p1="hello")
my_func(1,2,p3="hello")
my_func2(100,200)
my_func3(1,2,3,4,5,6,7) #p2 === touple with second and other valeues except first
my_func3(109,*[1,2,3,4,5])
p(type(my_func2(100,200))) #<class 'NoneType'>
p(type(my_func3(100,200))) #<class 'Str'> || return class

cursor = endTest()
##########################
startTest('keywords')

def func(p1=0, *p2, **p3):
    p(f"p1->{p1}")
    p(f"p2->{p2}")
    p(f"p3->{p3}")
    #p(p3.get('name')) #if p3 dosent exist return NoneType
    p('-------')

func()
func(10,20,p10=100) #p10:100 goes into dictionary
func(10,20,30,40)
func(name="tia",age="25")

tmp_list = []
for step in range(1,100):
    tmp_list.append(random.randint(1,100000))
func(*tmp_list)

my_args = {'p1':100,'name':'tia','age':25}
func(**my_args)
#func(*tmp_list,**my_args)

cursor = endTest()
