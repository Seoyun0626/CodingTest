a,b=list(map(int,input().split()))
num1=[]
num2=[]
result=[]
num=1
cnt1=0
while(num<=a):
    if(a%num==0):
        num1.append(num)
        cnt1+=1
    num+=1

num=1
cnt2=0
while(num<=b):
    if(b%num==0):
        num2.append(num)
        cnt2+=1
    num+=1
if(cnt1>cnt2):
    for i in range(cnt1):
        for j in range(cnt2):
            if(num1[i]==num2[j]):
                result.append(num1[i])
else:
    for i in range(cnt2):
        for j in range(cnt1):
            if(num2[i]==num1[j]):
                result.append(num2[i])

number=max(result)
number1=a/number
number2=b/number
print(number)
print(int(number*number1*number2))