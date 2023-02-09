import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
cnt = N + M
result = []
for _ in range(cnt):
    name = input().rstrip("\n")
    if name not in dic:
        dic[name] = 1
    else:
        dic[name] += 1
# print(dic)
for key, value in dic.items():
    if value == 2:
        result.append(key)

result.sort()
print(len(result))
for x in result:
    print(x)





