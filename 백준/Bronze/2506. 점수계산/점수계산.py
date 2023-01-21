N=int(input())
test=list(map(int,input().split()))
ans,score=0,0
for i in range(N):
    if(test[i]==0):
        score=0
    else:
        score+=1
        ans+=score
print(ans)