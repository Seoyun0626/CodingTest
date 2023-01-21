x,y,w,h=list(map(int, input().split()))
if(x>(w/2)):
    x=w%x
if(y>h/2):
    y=h%y
print(min(x,y))