#if
age = 3
if age > 18:
    print("your age is %d\n" % age)
elif age > 38:
    print('your age is %d\n' % age)
else:
    print("your age is %d\n" % age)


#for
l = [ 'a','b','c', ]
for x in l:
    print(x)

sum = 0
for x in range(100):
    sum = sum + x
print(sum)

#while
sum = 0
n = 0

while n < 100: 
    sum = sum + n
    n = n + 2
print(sum)

#break

n = 1

print("#######")
while n < 10:
    if n  == 9:
        break;
    print(n)
    n = n + 1
print("#######")

#continue


n = 0 
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

#dealloop

while True:
    pass
