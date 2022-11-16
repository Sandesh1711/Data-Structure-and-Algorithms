import math
n=23
flag=0
for i in range(2,int(math.sqrt(n))):
    if(n%i==0):
        print('Not a prime number')
        flag=1
        break
if flag==0:
    print('prime number')