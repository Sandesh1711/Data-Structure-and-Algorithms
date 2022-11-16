import numpy as np

ar = np.array([12,45,23,51,19,8])

def Bubblesort(ar):
    counter=1
    while counter<len(ar):
        for i in range(0,len(ar)-counter):
            if ar[i]<ar[i+1]:
                continue
            else:
                temp=ar[i]
                ar[i]=ar[i+1]
                ar[i+1]=temp
        counter=counter+1
result = Bubblesort(ar)
print(ar)