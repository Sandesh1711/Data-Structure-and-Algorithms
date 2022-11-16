n=154
m=n
sum1=0
while n>0:
    last = int(n%10)
    sum1=sum1+last**3
    n=int(n/10)

if sum1==m:
    print("Armstrong Number")
else:
    print("Not a Armstrong number")
