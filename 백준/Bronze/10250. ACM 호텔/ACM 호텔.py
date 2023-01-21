t=int(input())
for i in range(t):
    H,W,N=list(map(int,input().split()))
    if(N%H==0):
        print(int((H*100)+(N/H)))
    else:
        b=(N//H)+1
        a=N%H
        a=a*100
        print(a+b)