#숫자가 동일하여 구분이 필요할 떄 숫자을 입력받는 방식: enumerate 함수 사용하여 (value, index)


import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    result = 1
    N, index = map(int, input().split())
    nl = list(map(int, input().split())) # 맥스 확인
    q = deque()

    for idx, x in enumerate(nl):
        q.append((x, idx)) # value, index 값을 덱에 넣어놓음

    target_index = q[index][1] # 같은 값이 나왔을때 비교하기 위해 target_index

    while True:
        max_num = max(q)
        if q[0][0] == max_num[0]: #최댓값 맞춤
            if target_index == q[0][1]: # 찾는 인덱스가 나왔을 경우 + 최대값일떄
                print(result)
                break
            else: # 최대값인 경우 프린트 후 result + 1
                q.popleft()
                result += 1
        else:
            q.append(q.popleft())

        # max_num = max(nl) #최대값 갱신
        #
        # if q[0][0] == max_num: #맨앞과 최대값 비교
        #     if q[0][1] == target_index:
        #         result += 1
        #         print(result)
        #         break
        #     else:
        #         result += 1
        #         q.popleft()
        #         nl.remove(max_num)
        # else:
        #     q.append(q.popleft())








