import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    answer = 1
    dic = {}
    for _ in range(n):
        name, category = map(str, input().split())
        if category not in dic:
            dic[category] = 1
        else:
            dic[category] += 1
    for value in dic.values():
        answer *= (value + 1)
    answer -= 1
    print(answer)

