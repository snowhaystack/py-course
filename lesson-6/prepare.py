import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

gmail_user = 'xxx@gmail.com'
gmail_pwd = 'xxxxx'
html = '<html><body><b style="background:yellow;padding:5px;">TEST</b></body></html>'
message_html = MIMEText(html,"html")
message_image = MIMEImage(open(r'c:\temp\logo.jpg','rb').read())
message_pdf = MIMEApplication(open(r"c:\temp\example.pdf","rb").read(), Name='test.pdf')
message = MIMEMultipart()
message.attach(message_html)
message.attach(message_image)
message.attach(message_pdf)
message["From"]=gmail_user
message["To"]=gmail_user
message["Subject"]="test email"


server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(gmail_user, gmail_pwd)
server.ehlo()
server.send_message(message)
#server.sendmail((gmail_user, gmail_user, message.as_string())
server.quit()


import subprocess
from pprint import pprint

def execute_monitor(check_url):
    result = subprocess.run(['ping',check_url], capture_output=True, text=True)
    pprint(result)

check_url = 'google.com'
execute_monitor(check_url)

import re
str = 'Reply from 89.46.107.251: bytes=32 time=11ms TTL=56'
p1 = 'time=(\d+)ms'
pf = re.compile(p1)
pf.serach(str)



import subprocess
from pprint import pprint

def execute_monitor(check_url):
    result = subprocess.run(['ping',check_url], capture_output=True, text=True)
    out = result.stdout.split("\n")
    result = filter(lambda val: val.startswith("Reply"), out)
    print(len(list(result)))
    print(*result)
#https://regexr.com/
#https://regex101.com/
#https://rubular.com/r/DHt8RHjWYH
str.startswith
check_url = 'mattiafossati.com'
execute_monitor(check_url)


class Vehicle:
    def __init__(self,tire):
        print("init class " + str(self.__class__))
        self.tire = tire
    def start(self):
        print(id(self))
    def __del__(self):
        print("delete class " + str(self.__class__))

scooter = Vehicle(2)
print(id(scooter))
print(type(scooter))
scooter.start()
print(scooter.tire)
del scooter



class Vehicle:
    tank = 0
    __oil_viscosity = 0
    def __init__(self,tire_num):
        self.tires = [Tire(2.5,17) for i in range(0,tire_num)]
        #print("init class " + str(self.__class__))
        self.tire_num = tire_num
    def start(self):
        print(id(self))
    def __del__(self):
        #print("delete class " + str(self.__class__))
        pass
    def __add__(self,other):
        new = Vehicle(self.tire_num + other.tire_num)
        return new
    def __str__(self) -> str:
        return  f'Vehicle with {self.tire_num} tires'

class Tire:
    def __init__(self,pressure:float,diameter:int) -> None:
        self.pressure = pressure
        self.diameter = diameter
    def __str__(self) -> str:
        return  f'Tier pressure is {self.pressure}'

class Truck(Vehicle):
    def __init__(self):
        super().__init__(10)
    def __str__(self) -> str:
        return  f'Truck with {self.tire_num} tires'


scooter = Vehicle(2)
car = Vehicle(4)
car.tank = '100'
print(scooter.tank)#0
print(car.tank)#100
Vehicle.tank = 10
print(scooter.tank)#10
print(car.tank)#100 not 10 => assigned before


hybrid = scooter + car
print(hybrid.tire_num)
iveco = Truck()
print(iveco)
print(*iveco.tires)
print(Truck.__mro__)# resolution object