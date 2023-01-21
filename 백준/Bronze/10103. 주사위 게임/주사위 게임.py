n=int(input())
X=100
Y=100
for _ in range(n):
    a,b=map(int,input().split())
    if(a<b):
        X=X-b
    elif(a>b):
        Y=Y-a
    else:
        X=X
        Y=Y
print(X)
print(Y)