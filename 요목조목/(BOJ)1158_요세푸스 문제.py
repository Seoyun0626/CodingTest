# 부등호 범위에서 등호일 때 생각해보기 (indexerror 발생 시)

N, K = map(int, input().split())
num = []
result = []
check = K - 1
for i in range(1, N + 1):
    num.append(i)

result.append(num[check])
num.remove(num[check])

while len(num) != 0:
    check = check - 1 + K
    if check >= len(num):
        check = check % len(num)
    result.append(num[check])
    num.remove(num[check])

print("<", end="")
print(result[0], end="")
for i in range(1, len(result)):
    print(", ", end="")
    print(result[i], end="")
print(">")




