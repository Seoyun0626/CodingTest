N,K=list(map(int,input().split()))
result=1
for j in range(N,N-K,-1):
    result*=j
for i in range(K,0,-1):
    result/=i
print(int(result))