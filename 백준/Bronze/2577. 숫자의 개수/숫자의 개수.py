A=int(input())
B=int(input())
C=int(input())
time=[0]*10
num=A*B*C
length=len(str(num))
num=list(map(int,str(num)))
for i in range(length):
    a=num[i]
    time[a]+=1
for i in range(10):
    print(time[i])
