N=int(input())
last=0
for i in range(N):
    a,b=list(map(int,input().split()))
    last+=b % a
print(last)