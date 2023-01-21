a=[]
b=[]
for i in range(7):
    a.append(int(input()))
    
for i in range(7):
    if((a[i]%2)!=0):
        b.append(a[i])
           
if(len(b)==0):
    print('-1')
else:
    print(sum(b))
    print(min(b))
  