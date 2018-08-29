#how to get a 1..5 list
L = []

for x in range(5):
    L.append(x);
print(L)
#list generator formula #[]
print([ x for x in range(5)])

import os
print([ x for x in os.listdir('.')])

#selector #[0:]
str='Hello'
    #01234#
print(str[0:3])


#iterable : list、tuple、dict、set、str ,generator  # can for x in 
from collections import Iterable
print(isinstance('abc', Iterable))

#generater #()

ll = []
g = ( x for x in range(5))
for x in g:
    ll.append(x)
print(ll)

#generater #yield #change print to yield #different yield as a iterable type

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

#iterator #can be next() 

from collections import Iterator
isinstance((x for x in range(10)), Iterator) # True
isinstance([], Iterator) # list tuple dict set str is not iterator

#change iterable expect generator to iterator
isinstance(iter([]), Iterator)


