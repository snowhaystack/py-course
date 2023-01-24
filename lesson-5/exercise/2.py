#create decoration function
#create inner for decorate 
#function to decorate
import logging
from datetime import date
import time
def mydecor(func):
    def init_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        #handler = logging.StreamHandler()
        today = date.today() 
        handler = logging.FileHandler(f"C:\\wamp64\\www\\script\\py-course\\lesson-5\\exercise\\log-{today.year}-{today.month}-{today.day}.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def inner(*val, **val_dict):
        logger = init_logger()
        logger.info(f"paramter {val}, {val_dict}")
        start = time.time()
        val = func(*val, **val_dict)
        end = time.time()
        logger.info(f"{func} execution time => {end-start}")
        logger.info(f"result {val}")
        return val
    return inner


@mydecor
def sum(x,y):
    return f"{x =}, {y = }, sum =  {x+y}"
@mydecor
def subtraction(x,y):
    return f"{x =}, {y = }, subtraction =  {x-y}"
@mydecor
def multiplication(x,y):
    return f"{x =}, {y = }, multiplication =  {x*y}"
@mydecor
def division(x,divider):
    return f"{x =}, {divider = }, division =  {x/divider}"
@mydecor
def potency(x,index):
    for potency in range(0,index):
        potency = x*x
    return f"{x =}, {index = }, potency =  {potency}"


print(sum(1,10))
print(subtraction(100,8))
print(multiplication(5,7))
print(division(100,10))
print(potency(3,2))