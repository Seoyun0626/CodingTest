from collections import deque
import sys


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    word = list(map(str, input().split()))
    dq = deque()
    dq.append(word[0])
    for i in range(1, len(word)):
        if dq[0] >= word[i]:
            dq.appendleft(word[i])
        else:
            dq.append(word[i])
    result = "".join(dq)
    print(result)




