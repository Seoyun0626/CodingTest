import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for i in range(1, N + 1):
    dic[i] = input().rstrip()

new_dic = {v: k for k, v in dic.items()}



for _ in range(M):
    quiz = input().rstrip()
    if quiz.isnumeric():
        print(dic[int(quiz)])
    else:
        print(new_dic[quiz])


