N,M=list(map(int,input().split()))
num=list(map(int,input().split()))
result=[]
for i in range(N):
    first=num[i]
    for j in range(i+1,N,1):
        second=num[j]
        for k in range(j+1,N,1):
            sum=first+second+num[k]
            if(sum<=M):
                result.append(sum)

print(max(result))