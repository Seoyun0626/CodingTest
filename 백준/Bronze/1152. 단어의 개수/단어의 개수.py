a=input()
count=0
num=len(a)
for i in range(num):
    if(a[i]==' '):
        count+=1
if(a[0]==' '):
    count-=1
if(a[-1]==' '):
    count-=1
count+=1
print(count)