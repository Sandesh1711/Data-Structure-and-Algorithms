import numpy as np

a = np.array([-1,-7,4,2])
maxSum=0
for i in range(0,len(a)):
    sum=0
    for j in range(i,len(a)):
        sum=sum+a[j]
        maxSum=max(maxSum,sum)
print(maxSum)