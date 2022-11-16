import numpy as np
ar = np.array([12,45,23,51,19,8])

for i in range(1,len(ar)):
    current = ar[i]
    j=i-1
    while (ar[j]>current and j>=0):
        ar[j+1]=ar[j]
        j=j-1
    ar[j+1]=current

print(ar)