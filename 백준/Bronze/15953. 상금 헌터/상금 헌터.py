T=int(input())
for i in range(T):
    a,b=(map(int,input().split()))
    a_reward=0
    b_reward=0
    if(a==1):
        a_reward=500
    elif(a>=2 and a<=3):
        a_reward=300
    elif(a>=4 and a<=6):
        a_reward=200
    elif(a>=7 and a<=10):
        a_reward=50
    elif(a>=11 and a<=15):
        a_reward=30
    elif(a>=16 and a<=21):
        a_reward=10
    elif(a==0):
        a_reward=0
    if(b==1):
        b_reward=512
    elif(b>=2 and b<=3):
        b_reward=256
    elif(b>=4 and b<=7):
        b_reward=128
    elif(b>=8 and b<=15):
        b_reward=64
    elif(b>=16 and b<=31):
        b_reward=32
    elif(b==0):
        b_reward=0
    print((a_reward+b_reward)*10000)