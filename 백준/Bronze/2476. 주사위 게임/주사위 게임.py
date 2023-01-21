N=int(input())
reward=0
final=[]
for i in range(N):
    a,b,c=list(map(int,input().split()))
    if(a==b and b==c):
        reward=10000+(1000*a)
    elif(a!=b and b!=c and a!=c):
        reward=(max(a,b,c))*100
    else:
        if(a==b):
            reward=1000+(a*100)
        elif(a==c):
            reward=1000+(a*100)
        else:
            reward=1000+(b*100)
    final.append(reward)
print(max(final))