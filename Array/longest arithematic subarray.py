import numpy as np

ar = np.array([10,7,4,6,8,10,12,11])

pd = ar[1]-ar[0]
ans = 1
curr = 2
j=2
while (j<len(ar)):
    if (pd==ar[j]-ar[j-1]):
        curr =curr+1
    else:
        pd=ar[j]-ar[j-1]
        curr =2
    ans=max(ans,curr)
    j=j+1
print(ans)