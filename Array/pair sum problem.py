import numpy as np

a = np.array([1,2,6,4,5])
k=11
def pairSum(a,k):
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if (a[i]+a[j]==k):
                print(i,j)
                return True
    return  False

res = pairSum(a,k)
print(res)