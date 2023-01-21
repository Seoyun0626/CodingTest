a,b=list(map(int,input().split()))
MAX=a+b
TOTAL=MAX
for i in range(9):
    a,b=list(map(int,input().split()))
    TOTAL=TOTAL-a+b
    if(TOTAL>MAX):
        MAX=TOTAL
print(MAX)