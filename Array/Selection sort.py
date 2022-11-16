import numpy as np

ar = np.array([12,45,23,51,19,8])

def Selectionsort(ar):
    for i in range(0,len(ar)):
        for j in range(i+1,len(ar)):
            if ar[j]<ar[i]:
                temp=ar[j]
                ar[j]=ar[i]
                ar[i]=temp

    return ar
result =Selectionsort(ar)
print(result)
