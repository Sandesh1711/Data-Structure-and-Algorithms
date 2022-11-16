import numpy as np

a = np.array([1,2,0,7,2,0,2,2,9,1])
curr=None
i=1
while(i<len(a)):
    try:
        if (a[i]-a[i-1]>0)and(a[i]-a[i+1]>0):
            curr=a[i]
        else:
            curr=curr
    except IndexError as e:
        curr=curr
    i=i+1
print(curr)