N=int(input())
for i in range(N):
    for j in range(0,i+1,1):
        print('*',end="")
    for k in range(N*2-2*(i+1),0,-1):
        print(' ',end="")
    for p in range(0,i+1,1):
        print('*',end="")
    print()
for i in range(N-1,0,-1):
    for j in range(i,0,-1):
        print('*',end="")
    for k in range((N-i)*2,0,-1):
        print(' ',end="")
    for p in range(i,0,-1):
        print('*',end="")
    print()