while True:
    a,b=list(map(int,input().split()))
    if(a == 0 & b ==0 ):
        break
    else:
        if( a < b ):
            if( b % a == 0 ):
                print('factor')
            else:
                print('neither')
        elif( a > b ):
            if( a % b == 0 ):
                print('multiple')
            else:
                print('neither')