#coding=utf-8

import os
from multiprocessing import Process


#os.fork
'''
print("#########os.fork")

pid = os.fork()
if pid == 0:
	print("i am child pid is %d ppid is %d" % (os.getpid(),os.getppid()))
else:
	print("i am father pid is %d my child pid is %d" % (os.getpid(),pid))

'''

#multips
'''
print("#########multiprocess for windows")
def child_do(*args):
	print("child pid is %d get args is %s" % (os.getpid(),args))
	
p = Process(target=child_do,args=())
p.start()
p.join() #wait

'''

#process pool
'''
from multiprocessing import Pool
import os, time, random

def pool_func(name):
    print('run task %s pid is %s' % (name , os.getpid()))

pol = Pool(4)
for i in range(5):
    pol.apply_async(pool_func,args=(i,))
pol.close() # close before join
pol.join()

'''

#subprocess #exec


#pss communication

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



