n=12786
reverse=0
while n>0:
    last =int(n%10)
    reverse = reverse*10+last
    n=int(n/10);

print(reverse)
