for i in range(1,5):
    for j in range(0,i):
        print('*',end=' ')
    space = 2*4-2*i
    for j in range(1,space+1):
        print(' ',end=' ')

    for j in range(1,i+1):
        print('*',end=' ')
    print()
for i in range(5, 1,-1):
    for j in range(0, i):
        print('*', end=' ')
    space = 2 * 4 - 2 * i
    for j in range(1, space + 1):
        print(' ', end=' ')

    for j in range(1, i+1):
        print('*', end=' ')
    print()