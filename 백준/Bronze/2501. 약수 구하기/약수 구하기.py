N,K=list(map(int,input().split()))
factor=[]
for i in range(1,N+1,1):
    if(N % i == 0):
        factor.append(i)
if(len(factor)<K):
    print('0')
else:
    print(factor[K-1])