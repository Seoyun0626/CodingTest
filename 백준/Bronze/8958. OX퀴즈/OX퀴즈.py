T=int(input())
for i in range(T):
    result=0
    count=1
    grade=input()
    length=len(grade)
    if(grade[0]=='O'):
        result=1
    else:
        result=0
    for j in range(1,length,1):
        if(grade[j]!='O'):
            count=0
        else:
            if(grade[j-1]=='O'):
                count+=1
            else:
                count=1
        result+=count
    print(result)