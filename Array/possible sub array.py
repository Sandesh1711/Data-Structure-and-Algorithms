import numpy as np
a = np.array([-1,4,7,2])

for i in range(0,len(a)):
    for j in range(i,len(a)):
        for k in range(i,j+1):
            print(a[k],end=' ')
        print()