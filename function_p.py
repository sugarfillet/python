# high level fun
def abs(x):
    if x > 0:
        return x
    else:
        return -x

print(abs(-1))

def add(x,y,fn):
    return fn(x)+fn(y)

print(add(1,-2,abs))

#map

def f(x):
    return x * x
print(f(2))

r  = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)

print(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#reduce

from functools import reduce

def conn(x,y):
    return x+y
print(reduce(conn,['a','b','c']))
    
