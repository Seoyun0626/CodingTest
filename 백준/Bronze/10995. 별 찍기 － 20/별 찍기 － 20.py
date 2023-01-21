N=int(input())
if(N==1):
    print('*')
else:
    for i in range(1,N+1,1):
        if(i%2==1):
            print('*',end="")
            for j in range(N-1):
                print(' *',end="")
            print()
        else:
            for j in range(N):
                print(' *',end="")
            print()