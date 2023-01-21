N=int(input())

for i in range(N,0,-1):
    for k in range(0,N-i,1):
        print(' ',end="")
    for j in range(2*i-1):
        print('*',end="")
    print()