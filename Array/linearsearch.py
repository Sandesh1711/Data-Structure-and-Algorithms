import numpy as np

ar = np.array([1,4,6,8,5,3])
key=10
def linearsearch(ar,key):
    for i in range(0,len(ar)):
        if ar[i]==key:
            return (ar[i])
    return "Not found"
result = linearsearch(ar,key)
print('Value',result)

