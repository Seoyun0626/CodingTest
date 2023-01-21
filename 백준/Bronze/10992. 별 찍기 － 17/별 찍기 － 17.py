N=int(input())

for i in range(0,N-1):
    print(' '*(N-i-1),end='')
    if(i!=0):
        print('*',end='')
        print(' '*((2*i)-1),end='')
        print('*')
    else:
        print('*')

print('*'*(2*N-1))
    