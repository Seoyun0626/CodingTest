A_a,A_b,A_c,A_d=map(int,input().split())
B_a,B_b,B_c,B_d=map(int,input().split())
C_a,C_b,C_c,C_d=map(int,input().split())
X=(A_a+A_b+A_c+A_d)
Y=(B_a+B_b+B_c+B_d)
Z=(C_a+C_b+C_c+C_d)

if(X==3):
    print('A')
elif(X==2):
    print('B')
elif(X==1):
    print('C')
elif(X==4):
    print('E')
elif(X==0):
    print('D')
    
if(Y==3):
    print('A')
elif(Y==2):
    print('B')
elif(Y==1):
    print('C')
elif(Y==4):
    print('E')
elif(Y==0):
    print('D')

if(Z==3):
    print('A')
elif(Z==2):
    print('B')
elif(Z==1):
    print('C')
elif(Z==4):
    print('E')
elif(Z==0):
    print('D')