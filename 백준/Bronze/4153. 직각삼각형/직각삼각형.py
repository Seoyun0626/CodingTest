while True:
    A,B,C=list(map(int,input().split()))
    if(A==0 & B==0 & C==0):
        break
    else:
        if(C*C==A*A+B*B):
            print('right')
        elif(B*B==A*A+C*C):
            print('right')
        elif(A*A==B*B+C*C):
            print('right')
        else:
            print('wrong')