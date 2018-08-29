# higher level func # treat a func as a arg

# add(x,y,fn)
def abs(x):
    if x > 0:
        return x
    else:
        return -x

print(abs(-1))

def add(x,y,fn):
    return fn(x)+fn(y)

print(add(1,-2,abs))

#map # deal each element with func

#map(x^2,[])

def f(x):
    return x * x
print(f(2))

r  = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


#reduce # deal a group element with func according to func argc

#reduce(conn,[])

from functools import reduce

def conn(x,y):
    return x+y
print(reduce(conn,['a','b','c']))
    

#filter # similar to map 

#filter(odd,[])

def is_odd(x):
	return x % 2 == 1
print(list(filter(is_odd,[ x for x in range(10) ])))


#sorted 

#sorted([],key=str.lower) #str.lower is func name 

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
