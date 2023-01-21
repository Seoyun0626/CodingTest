N=int(input())
grade=list(map(int,input().split()))
M=max(grade)
for i in range(N):
    grade[i]=grade[i]/M*100
print(sum(grade)/N)