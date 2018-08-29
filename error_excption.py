#coding=utf-8

try:
    print('try...')
    r = 10 // 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
    #raise
finally:
    print('finally...')
print('END')

''' 
try except 可以只在最上层执行，会有详细的调用栈打印
'''
#raise
	# 抛出错误，自己不做处理，交由上层处理


#assert #相比print打点 会立即中断

print("assert test")
def foo(s):
    n = int(s)
    #assert n != 0, 'n is zero!'
    print("after assert")
    try:
	    return 10 / n
    except ZeroDivisionError as e:
	    print('except:',e)

def main():
    foo('0')
main()


#logging 最优秀

print("logging test")

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


#pdb

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

