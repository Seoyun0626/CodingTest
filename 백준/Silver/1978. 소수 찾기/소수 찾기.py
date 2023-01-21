N=int(input())
num=list(map(int,input().split()))
cnt=0
for i in range(N):
    count=0
    j=1
    while(j<=num[i]):
        if(num[i]%j==0):
            count+=1
            j+=1
        else:
            j+=1
    
    if(count==2):
        cnt+=1

print(cnt)
        