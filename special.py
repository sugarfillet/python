L = []

for x in range(5):
    L.append(x);
print(L)
#list generator
print([ x for x in range(5)])

import os
print([ x for x in os.listdir('.')])

#qiepian
str='Hello'
    #01234#
print(str[0:3])


#diedai iterable : list、tuple、dict、set、str ,generator 
from collections import Iterable
print(isinstance('abc', Iterable))

#generater

ll = []
g = ( x for x in range(5))
for x in g:
    ll.append(x)
print(ll)

#generater yield

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
for x in o:
    print(x)
