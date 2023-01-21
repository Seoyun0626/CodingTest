N=int(input())
result=[]
for i in range (N):
    result.append(int(input()))
result.sort()
for i in range(N):
    print(result[i])