# 시간 초과 deque풀기
# []입력 받으면 -> deque의 길이 1
# for-else -> break문을 통과하면 else실행
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    P = input().rstrip()
    n = int(input())
    num = input().rstrip()[1:-1].split(",")
    flag = 0
    queue = deque(num)

    if n == 0:
        queue = []
    # print(queue)

    for j in P:
        if j == "R":
            flag += 1
        elif j == "D":
            if len(queue) == 0:
                print("error")
                break
            else:
                if flag % 2 == 1:
                    queue.pop()
                else:
                    queue.popleft()
    # print(queue)
    else:
        if flag % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")







