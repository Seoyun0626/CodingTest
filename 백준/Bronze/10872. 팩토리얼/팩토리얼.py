N=int(input())
a=1
if N==0:
    print(1)
else:
    for i in range(N,0,-1):
        a=a*i  
    print(a)