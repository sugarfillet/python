

# thread 1. lock 2. multicpu  3. local var annoy
import threading

balance=0
lock = threading.Lock() # thread lock

def change(n):
    global balance
    balance += n
    balance -= n

def doThread(n):

    for i in range(10000):
        lock.acquire() # get 
        try:
            change(n)
        finally:
            lock.release() # rm

t1 = threading.Thread(target=doThread,args=(5,))
t2 = threading.Thread(target=doThread,args=(3,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
