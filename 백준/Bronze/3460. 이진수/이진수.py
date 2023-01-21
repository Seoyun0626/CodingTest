T=int(input())
result=0
for i in range(T):
    n=int(input())
    change=[]
    count=0
    while (n/2!=0):
        num=n%2
        n=n//2
        change.append(num)
        count+=1
    for j in range(count):
        if(change[j]==1):
            print(j,end=" ")
    print()