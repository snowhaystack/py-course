#create decoration function
#create inner for decorate 
#function to decorate
def mydecor(func):
    def inner(*val, **args):
        print(f'function execution {func = }')
        val = func(*val,**args)
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
def division(x,y):
    return f"{x =}, {y = }, division =  {x/y}"
@mydecor
def potency(x,y):
    for potency in range(0,y):
        potency = x*x
    return f"{x =}, {y = }, potency =  {potency}"


print(sum(1,10))
print(subtraction(100,8))
print(multiplication(5,7))
print(division(100,10))
print(potency(3,2))