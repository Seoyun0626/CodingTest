rest=[0]*42
count=0
for i in range(10):
    num=int(input())
    rest[num%42]+=1
for i in range(42):
    if(rest[i]>=1):
        count+=1
print(count)