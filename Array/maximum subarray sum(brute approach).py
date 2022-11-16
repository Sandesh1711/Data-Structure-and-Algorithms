import numpy as np

a = np.array([-1,7,4,2])
maxSum=0

for i in range(0,len(a)):
    for j in range(i,len(a)):
        sum=0
        for k in range(i,j+1):
            sum=sum+a[k]
            maxSum=max(maxSum,sum)
            #print(sum)

print(maxSum)