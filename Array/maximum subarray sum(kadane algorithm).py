import numpy as np
a = np.array([-1,4,-6,7,-4])
sum=0
i=0
maxSum=0
for i in range(0,len(a)):
    sum=sum+a[i]
    if sum<0:
        sum=0
    else:
        maxSum=max(maxSum,sum)
print(maxSum)