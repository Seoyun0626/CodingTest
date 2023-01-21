N=int(input())

for i in range(N):
    for j in range(N-1,i,-1):
        print(' ',end="")
    for k in range(0,i+1,1):
        print('*', end="")
    print()
for i in range(N-1):
    for j in range(i+1):
        print(' ',end="")
    for k in range(N-1-i,0,-1):
        print('*',end="")
    print()