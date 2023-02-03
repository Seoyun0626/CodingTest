# 딕셔너리도 시간 초과 가능
# 그럴때 {key, value}, {value, key} 값을 저장하여 key값 탐색으로만으로 해결할 수 있도록
# keyerror 발생 시 strip함수 잘 살펴보기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for i in range(1, N + 1):
    poke = input().rstrip()
    dic[i] = poke
    dic[poke] = i



for _ in range(M):
    quiz = input().rstrip()
    if quiz.isnumeric():
        print(dic[int(quiz)])
    else:
        print(dic[quiz])




# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# dic = {}
# for i in range(1, N + 1):
#     dic[i] = input().rstrip()
#
# new_dic = {v: k for k, v in dic.items()}
#
#
#
# for _ in range(M):
#     quiz = input().rstrip()
#     if quiz.isnumeric():
#         print(dic[int(quiz)])
#     else:
#         print(new_dic[quiz])
