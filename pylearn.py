'''
Created on 2017-6-22

@author: sWX451341
'''
===basic
from _abcoll import Iterable
from functools import reduce
import string
from numbers import Integral
import functools

#changable iterable 
#所有的数据类型 ： 分为  可变  可迭代
a=22
b=True
str='abc'
l=[1,2,3,4,]
t=(1,3,3,)
d={1:'a',2:'b',}
s=set(t)

all=[]
all.append(a)
all.append(b)
all.append(str)
all.append(l)
all.append(t)
all.append(d)
all.append(s)

print(all)

#iterable
for x in all:
    print(type(x),isinstance(x, Iterable))

for i,v in enumerate(l):
    print(i,v)
    
#list generator
print([i for i in range(1,10,3)])
print([m+n for m in 'abc' for n in 'xyz'])

#fib
def fib(n):
    a,b=0,1
    i=1
    while i<=n:
        print(b)
        a,b=b,a+b
        i += 1
    return b

print(fib(3))

#fib generator 
def fibg(n):
    a,b=0,1
    i=1
    while i<=n:
        yield b
        a,b=b,a+b
        i += 1
    #return b

print(next(fibg(3)),isinstance(fibg(3), Iterable))


#map
def x2(x):
    return x*x
print(list(map(x2,l)))

#reduce
def add(x,y):
    return x+y
print(reduce(add,l))


#filter
def is_odd(x):
    return x%2 == 1

print(list(filter(is_odd,l)))

#sorted
print(sorted([36, 5, -12, 9, -21], key=abs))

#return func() 闭包就是返回函数

def lasy_sum(*args):
    def sum():
        s=0
        for i in args:
            s += i
        return s
    return sum

#f = lazy_sum(1, 3, 5, 7, 9)

#匿名函数
print(list(map(lambda x:x*x,[1,])))


#deractor

def printa(func):
    def _print():
        for i in func():
            print(i)
    return _print

@printa
def getString():
    return [ x for x in  range(5)]

getString()


#pian func
print(int('1234',base=8))
int8 = functools.partial(int , base=8)
print(int8('1234'))



===class

# simple class
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        

aa=Student('a',5)
print(aa.age)
aa.age=8
print(aa.age)

#private and get set
class Student2(object):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name   
        
s2=Student2('B',6)

#print(s2.__name)
print(s2._Student2__name)#get private properity

print(s2.get_name())#get and set
s2.set_name('b')
print(s2.get_name())



#多态 开闭原则

class Animal(object):
    def run(self):
        print('animal run ...')
class Dog(Animal):
    def run(self):
        print('dog run ...')
    def __len__(self):
        return 100
class Husky(Dog):
    def __init__(self,weight,name):
        self.__weight = weight
        self.name = name
    def run(self):
        print('husky run ...')
class Abc(object):
    def run(self):
        print('abc run ...')
        
        
        
def run_twice(x):
    for i in range(2):
        x.run()
        
# type isinstance
print(type(Husky(5,'a')))
print(isinstance(Husky(5,'a'), (Animal,Dog)))

run_twice(Animal())
run_twice(Dog())#多态
run_twice(Abc())#鸭子类型： file-like object

print(dir('ABC'))
print('ABC'.__len__())
#define __len__ dog
print(dir(Dog()))
print(Dog().__len__())
print(len(Dog()))

#get set ha attr()
hs = Husky(55,'a')
print(hasattr(hs, '__weight')) #can't get private property
print(hasattr(hs, 'name'))
print(getattr(hs, 'name'))
print(setattr(hs, 'name','asdfsf'))
print(getattr(hs, 'name'))


#class property and instance property

class Father(object):
    name='father property'


f = Father()
print(f.name)
f.abc='abc'
print(f.abc)
f.name='f.property name'
print(f.name)
del f.name
print(f.name)
       
===class-ad

# -*- coding: utf-8 -*-

#static_l dynamic_l 
#python 可以动态的给实例添加属性（方法）
#python 对于数据类型的要求不严格 
#python 鸭子类型
#动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的

#限制属性绑定
class Student(object):
    __slots__ = ('name','age')

s = Student()
s.name = 9
print(s.name)  
#AttributeError: 'Student' object has no attribute 'abc  
#s.abc = 1
#print(s.abc)

# 子类属性绑定的限制 ，如果不声明slots，则不继承

class XiaoStudent(object):
    __slots__ = () #AttributeError: 'XiaoStudent' object has no attribute 'abc'
    pass

xiao = XiaoStudent()

#xiao.abc = 1
#print(xiao.abc)


#==========
# 属性绑定 限制  还是不够  s.score=9 ，没有对参数进行限制
# 可以设置get set 方法 ，来实现属性检查，但是方法的 调用显得繁琐 ，
#采用直接的简单的get set方法  @property

class Student1(object):
    
    
    #def getter
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s1 = Student1()
s1.score = -1
print(s1.score)

#多重继承  和  定制类  简单了解
#枚举类
#元类


===execption
# -*- coding: utf-8 -*-
#简单的错误判断机制  太繁琐了 
#出现了 try catch finally:

#不需要在每个可能出错的地方去捕获错误，只要在合适的（最上的）层次去捕获错误就可以了

try : 
    print('try start')
    r = 10 / int('1')
    print('result:' , r)
except ValueError as e:
    print('ValueError:', e)    
except ZeroDivisionError as e:
    print('get zero divison error:',e)
else:
    print('no error')
finally:
    print('finally')
   
   
#自定义 error 并抛出
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

try:
    foo('0') 
except FooError as e :
    print(e)

===file

# -*- coding: utf-8 -*-

filename = 'hello'
with open(filename,'r') as f:
    for line in f:
        print(line)
        
#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object


with open(filename,'w') as f:
    f.write('nihia')


#StringIO/BytesIO write
from io import StringIO

f = StringIO()
f.write('hello')
f.write('wrold')

print(f.getvalue())

#StringIO/BytesIO read

f = StringIO("hello!\nMIAOMI!")
print(f.read())
while 1:
    s = f.readline()
    if s=='':
        break
    print(s)
    


#OS

import os
print(type(os.environ))
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join('/Users/michael', 'testdir'))
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


#json 
import json



d={ 'name':'song','age':5,'school':'nuist' }
print(json.dumps(d))
json_str = '{"age": 5, "name": "song", "school": "nuist"}'
print(json.loads(json_str))


# instance xuliehua

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
def student2dict(std):
        return {
        'name': std.name,
        'age': std.age,
        'score': std.score
        }
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s = Student('Bob', 20, 88)
#print(json.dumps(s),)
print(json.dumps(s, default=student2dict))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))



===p1


from multiprocessing import Process
import os

#create child process

def child_func():
    print("child process is %s" % os.getpid())
    
print("current process is %s" % os.getpid())
p=Process(target=child_func)
print('child is starting...')
p.start()
p.join(5)
print('child is done')


#process pool
from multiprocessing import Pool
import os, time, random

def pool_func(name):
    print('run task %s pid is %s' % (name , os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('run task %s time is %f s' %(name , (end - start)))
    
print('current pid is %s' % os.getpid())
pol = Pool(4)
for i in range(5):
    pol.apply_async(pool_func,args=(i,))
print('waiting for subprocess done')
pol.close()
pol.join()
print('all done')



===p2

'''
Created on 2017-6-23

@author: sWX451341
'''

#进程间通信

from multiprocessing import Process ,Queue
import os ,time ,random

def write(q):
    print('write process is %s' % os.getpid())
    for v in 'abc':
        q.put(v)
        time.sleep(random.random())
        
def read(q):     
    print('read process is %s' % os.getpid())
    while 1:
        value = q.get(True)
        print('get " %s " form queue' % value)
        
if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write ,args=(q,))
    pr = Process(target=read ,args=(q,))
    
    pw.start()
    pr.start()
    
    pw.join()
    pr.terminate()
    
===t1
  
'''
Created on 2017-6-23

@author: sWX451341
'''
#create a thread

import time ,threading

def thread_do():
    print('thread %s is running ..' % threading.Thread().name)
    for i in range(5):
        print('thread %s >> %s' % (threading.Thread().name,i))
        time.sleep(1)
    print('thread %s is over ' % threading.Thread().name)
    
print(threading.current_thread().name)
t  = threading.Thread( target=thread_do, name='doThread')
t.start()
t.join()
print('%s is over'  % threading.current_thread().name)

===t2

'''
Created on 2017-6-23

@author: sWX451341
'''

#Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
#多个Python进程有各自独立的GIL锁，互不影响。
#python 每一个进程都有一个独立个gil锁，
#这就保证了一个进程的所有线程不能跑到别的cpu执行

import threading

balance=0
lock = threading.Lock()

def change(n):
    global balance
    balance += n
    balance -= n
    
def doThread(n):
    
    for i in range(10000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()

t1 = threading.Thread(target=doThread,args=(5,))
t2 = threading.Thread(target=doThread,args=(3,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)




#一个ThreadLocal变量虽然是全局变量，
#但每个线程都只能读写自己线程的独立副本，互不干扰。
#ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

import threading

local = threading.local()

def process_student():
    name = local.name
    print(name)

def process_thread(name):
    local.name = name 
    process_student()


t11 = threading.Thread(target=process_thread,args=('aaa',))
t22 = threading.Thread(target=process_thread,args=('bbb',))
t11.start()
t22.start()
t11.join()
t22.join()





==tcp_c
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('huawei.com',80))

s.send(b'GET / HTTP/1.1\r\nHost: www.huawei.com\r\nConnection: close\r\n\r\n')


buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close()


#print(data)

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

with open('sina.html', 'wb') as f:
    f.write(html)
    
    
==tcp_s

#tcp sock.sock() .send() .recv() .close() .bind() .listen() .accept()
import socket
import threading


def tcplink(sock ,addr ):
    pass
#    print('i am the server thread i get $s:%s ' % addr)
    sock.send(b'welcome !\n')
    while 1:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello , %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('i am the server '+threading.Thread().name+' i am over')
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))

s.listen(5)
print('Waiting for connection...')

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr),name='XIANCHENG')
    t.start()
    

    
        
==tcp_sc

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))

print(s.recv(1024).decode('utf-8'))

for data in [b'aaa',b'bbb',b'ccc']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()

==udp_s

import socket


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.1.1.1',9998))


print('bond udp on p 9998')

while 1:
    data , addr = s.recvfrom(1024)
    print('get message from client ')
    s.sendto((b'hello , %s!' % data),addr)
    


==udp_sc

import socket


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = ('127.1.1.1',9998)

for data in [b'aaa',b'ccc']:
    s.sendto(data,addr)
    print(s.recv(1024).decode('utf-8'))
    
    
s.close()



==sqlite

import sqlite3


conn = sqlite3.connect('test.db')
cursor = conn.cursor()

#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.commit()
conn.close()

==modules

#datetime class
#from <module> import <func/class>
from collections import defaultdict, deque, namedtuple, OrderedDict
from datetime import datetime
import time
#get now
date = datetime.now()
print(datetime.now())
print(type(date))
#contruct time
dt = datetime(2017, 6, 27, 12, 20)
print(dt)
#time -> stamp
stamp = time.mktime(dt.timetuple())
print(stamp)
#stamp -> time
print(datetime.fromtimestamp(stamp))
#str -> time
str = '2015-6-1 18:19:59'
format = '%Y-%m-%d %H:%M:%S'
cday = datetime.strptime(str , format)
print(cday)
#time -> str
str1 = datetime.strftime(cday,format)
print(str1)

#namedtuple


Point = namedtuple('Point', ('x','y'))
print(Point)
p = Point(1,2)
print(p,isinstance(p, tuple))


#deque


q = deque(['1','2','3'])
q.append('4')
q.appendleft('0')
print(q)

#defaultdict

d = defaultdict(lambda: 'dd-no')
d['k1'] = 'v1'
print(d)
print(d['k2'])

#orderedict

d = dict([(1,'a'),(2,'b'),(3,'c')])
print(d)

od = OrderedDict([(1,'a'),(2,'b'),(3,'c')])
print(od)

#base64 主要用于编码少量文本，用于传输
#struct 实现基本数据类型到字节的映射
#haslib 用于单项加密
#itertools 迭代工具
#contentlib 上下文装饰器
#urllib htpp请求工具
#xml sax xml解析
#htmlparser 
    
    






