N=int(input())
result=[]
for i in range(N):
    result.append(list(map(int,input().split())))
result.sort(key=lambda x:(x[1],x[0]))
for i in (result):
    print(i[0],i[1])