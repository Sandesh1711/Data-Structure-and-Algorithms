n=int(input("enter the number of row:"))
m=int(input("enter the number of columns:"))


for i in range(0,n):
    for j in range(0,m):
        if i==0 or i==n-1:
            print('*',end='')

        elif j==0 or j==m-1:
            print('*',end='')

        else:
            print(' ',end='')

    print()
