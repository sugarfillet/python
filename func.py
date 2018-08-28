def my_abs(x):
    if x >=0:
        return x
    else:
        return -x

print(my_abs(-1))


#power

def my_power_1 (x ,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(my_power_1(2,3))

#power 2 # default arg
def my_power_1 (x ,n=3):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(my_power_1(2))
print(my_power_1(2,4))

# special fun args
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f1(1,2,3,4,x=1)

#digui

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(100))








