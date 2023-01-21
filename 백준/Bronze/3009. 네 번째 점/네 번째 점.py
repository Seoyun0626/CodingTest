A_a,A_b=map(int,input().split())
B_a,B_b=map(int,input().split())
C_a,C_b=map(int,input().split())
if((B_a != C_a) & (B_b != C_b)):
    P_a=(B_a+C_a)
    P_b=(B_b+C_b)
    X_a=(P_a-A_a)
    X_b=(P_b-A_b)
if((B_a != A_a) & (B_b != A_b)):
    P_a=(B_a+A_a)
    P_b=(B_b+A_b)
    X_a=(P_a-C_a)
    X_b=(P_b-C_b)
if((C_a != A_a) & (C_b != A_b)):
    P_a=(C_a+A_a)
    P_b=(C_b+A_b)
    X_a=(P_a-B_a)
    X_b=(P_b-B_b)
print(X_a,X_b)