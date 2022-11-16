import  numpy as np

a = np.array([2,4,7,11,14,16,20,21])
low = 0
high = len(a)-1
key=31
def SumPair(a,low,high):
    for i in range(0,len(a)):
        if a[low]+a[high]>key:
            high=high-1
            low=low
        elif a[low]+a[high]<key:
            low=low+1
            high=high
        else:
            return low,high

res = SumPair(a,low,high)
print(res)