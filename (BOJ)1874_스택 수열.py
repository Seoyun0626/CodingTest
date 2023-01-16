import sys

input = sys.stdin.readline
stack = []
answer = []
flag = False
point = 1

n = int(input())

for i in range(n):
    num = int(input())
    while point <= num:
        stack.append(point)
        answer.append("+")
        point += 1
    if (stack[-1] == num):
        stack.pop()
        answer.append("-")
    else:
        flag = True
        break
if (flag == False):
    for x in answer:
        print(x)
else:
    print("NO")



    


    
