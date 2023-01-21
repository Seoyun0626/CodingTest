cur_h,cur_m=list(map(int,input().split()))
need_t=int(input())

if(cur_m+need_t>=60):
    final_h=cur_h+((cur_m+need_t)//60)
    if(final_h>=24):
        final_h=final_h%24
    final_m=(cur_m+need_t)%60
else:
    final_m=cur_m+need_t
    final_h=cur_h
print(final_h,final_m)    