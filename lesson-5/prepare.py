import os
from functools import reduce
path = r"c:\backup"
counter = 0
for root, dirs, files in os.walk(path):
    print(files)
    counter += len(files)
print(counter)
#list compreinsion
#lamda function
#reduce
#count = [lambda counter:counter += len(files) for root, dirs, files in os.walk(path) ]
count = reduce( lambda a,b: a+b, [len(files) for _,_,files in os.walk(path) ])
print(count)
#get couple of elements in iterable element and apply function
list_1 = ['one','two','three',4,5]
#map => apply operation on lists elements
#reduce => apply function on lists elements
reduce(lambda firt_val,second_val: f'{firt_val}+{second_val}',list_1,'init => ')
#lambda function on all list
#"<select><option>one</option></select>"
result = reduce(lambda firt_val,second_val: f'{firt_val}<option>{second_val}</option>',list_1,'<select>') + '</select>'
result_map = map(lambda val: f'<option>{val}</option>',list_1)
print(*result_map)#dont return concat elements but another list
print(list(result_map))#print complete list
#decoration function
def mydecor(func):
    def inner():
        print('inner decorator start')
        val = func()
        print('inner decorator start')
        return val
    return inner()
@mydecor #add functionalities to function
def test():
    print('test')
test()#output => inner decorator start \n test \n inner decorator end
##################return same result###########################
def mydecor1(func):
    def inner(*val):
        return func(*val)
    return inner

@mydecor1
def test1(x,y):
    return f'{x = },{y =}, sum = {x+y}'
print(test1(900,43))# x =900, y = 43, sum = 943 => without @mydecorator
##################return result###########################
def mydecor2(func):
    def inner(*val):
        print('decorated')
    return inner

@mydecor2
def test2(y):
    return f'{y =}'
print(test2('xxx'))# decorated
##################return result with decoration###########################
def mydecor3(func):
    def inner(*val,**kwargs):
        print('init')
        val = func(*val,**kwargs)
        print('end')
        return val
    return inner

@mydecor3
def test3(y):
    return f'{y =}'
print(test3('xxx'))# init \n end \n y ='xxx'
##################return result with time###########################
import time
def mydecor4(func):
    def inner(*val, **kwargs):
        start = time.time()
        val = func(*val, **kwargs)
        end = time.time()
        print(f"{func} ha impiegato {end-start}")
        return val
    return inner

@mydecor4
def test4(x,y):
    time.sleep(3)
    return f"{x =}, {y = }, sum =  {x+y}"

@mydecor4
def test5(y):
    time.sleep(1)
    return f"{y =}"

print(test4(900,43))
print(test5("yy"))
#<function test at 0x000002D8115F0940> ha impiegato 3.0164852142333984
#x =900, y = 43, sum = 943
#<function test_new at 0x000002D8115F1510> ha impiegato 1.027409315109253
#y ='yy'
import requests
from pprint import pprint
response = requests.get('https://api.github.com/users/snowhaystack')
print('-----------')
print(response.text)
print('-----------')
print(response.json())
print('-----------')
print(response.json()['html_url'])
print('-----------')
print(response.headers)
print('-----------')
print(response.headers['Content-Type'])

url = 'https://api.github.com/search/repositories'
param = {'q':'requests+lenguage:python'}
response  =requests.get(url,params=param)
response_json = response.json()
items = response_json['items']
for item in items:
    pprint(item['name']) #json formatted
    pprint(item['description'])


test_url_post = 'http://httpbin.org/post'
data1 = {'name':'xxxx'}
response1 = requests.post(test_url_post,data1)
pprint(response1.json())

test_url_delete = 'http://httpbin.org/delete'
data2 = {'id':1000}
response2 = requests.post(test_url_delete,data2)
pprint(response2.json())

import smtplib
from pprint import pprint
import datetime
import schedule
import time
from email.mime.text import MIMEText #audio,image etc...



gmail_user = 'xxx@gmail.com'
gmail_pwd = 'xxxxx'
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(gmail_user, gmail_pwd)
pprint(server.ehlo()) #if smtp.gmail.com at your service can use this server for send email
email = r'Subject:test\ntesting py email\n'
server.sendmail(gmail_user,gmail_user)
server.quit()

#automated quit
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: 
    server.login(gmail_user, gmail_pwd)
    mail = "Subject:test Invio\nquesta e una mail\n"
    server.sendmail(gmail_user, gmail_user, mail)

#send actual time
def send_time_by_email1():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_pwd)
        mail = f"Subject:Actual Time\nTime: {datetime.datetime.now().hour}\n"
        server.sendmail(gmail_user, gmail_user, mail)
send_time_by_email1()




#send txt file
def send_time_by_email3():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_pwd)
        
        message = MIMEText('<html><body><b style="background:yellow;padding:5px;">TEST</b></body></html>',"html")
        message["From"]=gmail_user
        message["To"]=gmail_user
        message["Subject"]="test email"

        
        server.sendmail(gmail_user, gmail_user, message.as_string())

send_time_by_email3()

#schedule every 5 seconds
def send_time_by_email2():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_pwd)
        mail = f"Subject:Actual Time\nTime: {datetime.datetime.now().hour} e {datetime.datetime.now().minute} e {datetime.datetime.now().second}\n"
        server.sendmail(gmail_user, gmail_user, mail)

schedule.every(5).seconds.do(send_time_by_email2)
schedule.every(5).seconds.do(send_time_by_email2)
while True:
    schedule.run_pending()
    time.sleep(1)