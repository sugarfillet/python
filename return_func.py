#coding=utf-8

# retrun func

#do args sum

def summ(*args):
	s = 0 
	for x in args:
		s = s + x
	return s

print(summ(1,2,3,4,5))

#delay return 

def delay_summ(*args):
	def summm():
		s = 0
		for x in args:
			s = s + x
		return s
	return summm

ds = delay_summ(1,2,3,4,5)
print("ds type is %s\n" % str(type(ds)))
print("exec ds return %d\n" % ds()) # here do ds


"""
closure

我们在函数lazy_sum中又定义了函数sum，并且，
内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
*当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，*
这种称为“闭包
"""

#lamdba # lambda args: func_do 

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


#decorator # return wrapper #

def log(func):
	def wrapper(*args,**kw):
		print("call %s" % func.__name__)
		return func(*args, **kw)
	return wrapper


@log
def now():
	print("2018-8-29")

now()

