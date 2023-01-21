N=int(input())
arr=[]
result=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
for i in range(N):
    k=1
    for j in range(N):
        if(arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]):
            k+=1
    print(k,end=' ')