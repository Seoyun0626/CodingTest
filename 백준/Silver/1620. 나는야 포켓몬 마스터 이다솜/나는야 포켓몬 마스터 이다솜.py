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