# 정답은 나왔지만 시간 초과..
# 시간초과 이유 : insert,remove 함수 -> O(n) 시간 필요
# 시간초과 해결 : stack활용 -> append, pop 함수 -> O(1) 시간
# 커서를 기준으로 stack 2개 활용

import sys
input = sys.stdin.readline

stack_l = list(input().rstrip())
stack_r = []
M = int(input())
for _ in range(M):
    cmd = list(input().split())
    if cmd[0] == "L":
        if stack_l:
            stack_r.append(stack_l.pop())
    elif cmd[0] == "D":
        if stack_r:
            stack_l.append(stack_r.pop())
    elif cmd[0] == "B":
        if stack_l:
            stack_l.pop()
    else:
        stack_l.append(cmd[1])

stack_l.extend(reversed(stack_r))
print("".join(stack_l))





