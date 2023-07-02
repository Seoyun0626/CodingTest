# 맨 왼쪽, 맨 오른쪽 말 -> deque 사용
# 추가 : append, appendleft, 삭제 : pop, popleft
# 리스트를 문자열로 : join사용

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




