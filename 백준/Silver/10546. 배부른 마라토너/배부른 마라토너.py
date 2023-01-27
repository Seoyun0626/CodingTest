import sys
input= sys.stdin.readline

N = int(input())
li = dict() 
for _ in range(N):
    name = input().rstrip() 
    if name not in li.keys(): 
        li[name] = 1 
    else:
        li[name] += 1 


for _ in range(N-1):
    name = input().rstrip() 
    if name in li.keys(): 
        li[name] += 1

for key, values in li.items():
    if values %2 == 1: 
        print(key)
        break