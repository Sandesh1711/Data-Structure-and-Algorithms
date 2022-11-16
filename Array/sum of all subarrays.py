import numpy as np

ar = np.array([1,2,2])
sum=0
for i in range(0,len(ar)):
    sum=0
    for j in range(i,len(ar) ):
        sum = sum+ar[j]
        print(sum)

print(sum)