T = int(input())

def empty():
    if(len(stack) != 0):
        return 0
    else:
        return 1

for i in range(T):
    flag = False
    line = list(map(str, input()))
    stack = []
    for i in range(len(line)):
        if (line[i] == '('):
            stack.append('(')
        else:
            if (empty() == 0):
                stack.pop()
            else:
                flag = True
                break
    if (flag == False):
        if (len(stack) == 0):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

