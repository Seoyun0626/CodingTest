N=int(input())
for i in range(N):
    r,e,c=list(map(int,input().split()))
    total=e-c
    if(r>total):
        print('do not advertise')
    elif(r<total):
        print('advertise')
    else:
        print('does not matter')