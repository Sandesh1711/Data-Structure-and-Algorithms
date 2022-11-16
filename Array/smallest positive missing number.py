import numpy as np

a = np.array([0,-9,1,3,-4,5])
b=a>0
b.astype(np.bool)
print(b)
ans=0

for i in range(1,len(a)):
    if b[i]!=False:
        b[a[i]]=True
print(ans)
