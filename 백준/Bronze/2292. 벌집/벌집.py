N=int(input())
if(N==1):
    i=1
else:
    for i in range(1,N+1,1):
        if((i*3*(i-1)+1)>=N):
            break
print(i)
