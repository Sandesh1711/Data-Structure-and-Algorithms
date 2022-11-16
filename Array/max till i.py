import numpy as np

ar = np.array([1,10,5,4,6,18])

max1=0
for i in range(0,len(ar)):
    if ar[i]<max1:
        max1=max1
    else:
        max1=ar[i]

print(max1)