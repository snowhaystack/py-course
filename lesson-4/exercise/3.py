#fibonacci fn
import time
t1 = time.time()
def fibonacci(n):
    if n in {0,1}:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

res = [fibonacci(n) for n in range(60)]
print(res)
t2 =time.time()
print(f'Execution time {t2-t1:2f}')