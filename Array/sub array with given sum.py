import numpy as np

a = np.array([1,2,3,7,5])
key = 1

def subArraySum(a,key):
    for i in range(0,len(a)):
        currSum = a[i]
        if (currSum==key):
            return i    
        else:
            for j in range(i+1,len(a)):
                currSum=currSum+a[j]
                if (currSum==key):
                    return i,j

res = subArraySum(a,key)
print(res)