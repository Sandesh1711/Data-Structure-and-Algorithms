import numpy as np
ans=0
a = np.array([1,5,4,9,3,8,5,9])

def First_repeat(a):
    global ans
    flag=0
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                ans = i
                flag=1
            else:
                pass

        if flag == 1:
            break
    return ans
res = First_repeat(a)
print(res)