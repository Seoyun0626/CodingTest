N=int(input())
for i in range(0,N,1):
    for j in range(0,i,1):
        print(" ",end="")
    for k in range(N-i,0,-1):
        print("*",end="")
    print()