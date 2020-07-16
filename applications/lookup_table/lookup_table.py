# Your code here
import math
import random
#build a cache dict
cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    print(f'first: {v}')
    v = math.factorial(v)
    print(f'second: {v}')
    v //= (x + y)
    print(f'third: {v}')
    v %= 982451653
    print(f'fourth: {v}')
    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    #is in the cache? if not, compute it then put it in the cache
def slow_inner(x,y):    
    double = (x,y)
    if double not in cache:
        v = math.pow(x, y)
        #print(f'first: {v}')
        v = math.factorial(v)
        #print(f'second: {v}')
        v //= (x + y)
        #print(f'third: {v}')
        v %= 982451653
        #print(f'fourth: {v}')
        cache[double] = v
        return cache[double]
    return slow_inner(x,y)



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
