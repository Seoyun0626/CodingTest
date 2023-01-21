a=[]
N=int(input())

for i in range(N):
    a.append(int(input()))
if(sum(a)>N//2):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')