import numpy as np

ar = np.array([2,57,85,32,3,4,5,44,10])
key=20
for i in range(0,len(ar)):
    if ar[i]==key:
        print(ar[i])
        print('Index found at :' ,i)
        i=i+1
    else:
        continue
