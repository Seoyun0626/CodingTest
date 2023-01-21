A=int(input())
B=int(input())
C=int(input())
D=int(input())
P=int(input())

X=A*P
if(C>P):
    Y=B
else:
    Y=B+D*(P-C)
print(min(X,Y))