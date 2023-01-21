N,M,K=list(map(int,input().split()))
first=0
while (N >= 2 and M >= 1):
    first+=1
    N-=2
    M-=1
cal=N+M
if((cal)>K):
    first=first
else:
    while(cal<K):
        first-=1
        N+=2
        M+=1
        cal=N+M
print(first)