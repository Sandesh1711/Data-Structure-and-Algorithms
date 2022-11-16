import numpy as np

#a = np.array([4,-4,6,-6,10,-11,12])
a= np.array([-1,4,-6,7,5,-4])
b=np.copy(a)
for i in range(0,len(a)):
    a[i]=-a[i]
non_contributing = max(a)
sum=0
maxSum=0
for i in range(0,len(a)):
        sum=sum+a[i]
        if sum<0:
            sum=0
        maxSum = max(maxSum,sum)
res = maxSum+non_contributing
print(res)