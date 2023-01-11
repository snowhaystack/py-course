#primary number list
import time
#all return true if all elements are not False
PRIMARY_NUMER = 1000
t1 = time.time()
is_primary = [number for number in range(PRIMARY_NUMER) 
                if all(number%checker for checker in range(2,number))]
t2 =time.time()
print(f'Execution time {t2-t1:2f}')
