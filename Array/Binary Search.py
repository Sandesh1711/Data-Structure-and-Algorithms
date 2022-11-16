import numpy as np
ar = np.array([1,3,5,8,9,2,10,4])
ar.sort()
key=9

#[1,2,3,4,5,8,9,10]
def BinarySearch(ar,key):
    low = 0
    high = len(ar)
    while low<=high:
        mid =int( (low + high) / 2)
        if ar[mid]==key:
            return (ar[mid])
        elif ar[mid]>key:
            low=0
            high=mid-1
        else:
            low=mid+1
            high=high

    return 0

result = BinarySearch(ar,key)
if result==0:
    print("Value not found")
else:
    print("Value",result)