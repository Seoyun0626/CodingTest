N=int(input())

for i in range(1,N+1,1):
    for j in range(0,i,1):
        print('*',end="")
    print()
for i in range(N-1,0,-1):
    for j in range(i,0,-1):
        print('*',end="")
    print()
        