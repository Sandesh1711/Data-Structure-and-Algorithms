import numpy as np

arr = np.array([1,2,3,4,5])
# ar = np.array([])
#
# def Rotation(x,ar):
#     i = len(x)
#     while i>0:
#         ar=np.append(ar,[x[i-1]])
#         i=i-1
#     return ar
# result = Rotation(arr,ar)
# print(result)

d=4
n=len(arr)
temp=[]
i=0
while i<d:
    temp=arr[d:]
    i=i+1
arr=np.append(temp,arr[:d])
print(arr)

