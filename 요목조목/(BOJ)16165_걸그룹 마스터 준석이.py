# rstrip했으면 비교할 때 전부다 rstrip해주기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
group = {}
for i in range(N):
    group_name = input().rstrip()
    num =int(input())
    for _ in range(num):
        name = input().rstrip()
        group[name] = group_name


for j in range(M):
    word = input().rstrip()
    kind = int(input())
    if kind == 0:
        member = []
        for key, value in group.items():
            if value == word:
                member.append(key)
            member.sort()
        for x in member:
            print(x)


    else:
        for key, value in group.items():
            if key == word:
                print(value)
                break




