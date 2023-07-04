# 그리디 = 정렬

import sys

input = sys.stdin.readline
t = int(input())


for _ in range(t):
    n = int(input())
    score = []
    cnt = 1
    top = 0
    for i in range(n):
        write, speak = map(int, input().split())
        score.append((write, speak))
    score_sort = sorted(score)
    # print(score_sort)

    for i in range(1, len(score_sort)):
        if score_sort[i][1] < score_sort[top][1]:
            top = i
            cnt += 1
    print(cnt)


# 시간 초과 코드

# for _ in range(t):
#     n = int(input())
#     write_arr = []
#     speak_arr = []
#     cnt = 0
#     for _ in range(n):
#         write, speak = map(int, input().split())
#         write_arr.append(write)
#         speak_arr.append(speak)
#     print(write_arr, speak_arr)
#     for i in range(n):
#         flag = 1
#         for j in range(n):
#             if write_arr[i] > write_arr[j] and speak_arr[i] > speak_arr[j]:
#                 flag = 0
#                 break
#         if flag:
#             # print(i)
#             cnt += 1
#     print(cnt)

