A_a,A_b=list(map(int,input().split()))
B_a,B_b=list(map(int,input().split()))
C_a,C_b=list(map(int,input().split()))
D_a,D_b=list(map(int,input().split()))

X=A_a+A_b
Y=X-B_a+B_b
Z=Y-C_a+C_b
W=Z-D_a+D_b

a=[X,Y,Z,W]
print(max(a))