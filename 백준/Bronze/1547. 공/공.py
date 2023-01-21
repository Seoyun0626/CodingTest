M=int(input())
ball=1
for _ in range(M):
    a,b=list(map(int,input().split()))
    if(ball != a and ball != b):
        ball=ball
    elif(ball == a):
        ball=b
    elif(ball == b):
        ball=a
    else:
        ball=-1
print(ball)