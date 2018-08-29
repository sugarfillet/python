#coding=utf-8

#read a file
'''
try:
    f = open('/root/abc', 'r')
    print(f.read())
except	FileNotFoundError as e:
    print(e)
finally:
    if f:
        f.close()
'''

#simple # no f.close()

with open('/root/abc', 'r') as f:
	for line in f.readlines():
	    print(line.strip()) # 把末尾的'\n'删掉


#stringio # write a str in mem

from io import StringIO

f = StringIO('hello!\nHi!\nGoodbye!')
for line in f.readlines():
	print(line.strip())

#bytesio # write bin in meme

from io import BytesIO

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())


