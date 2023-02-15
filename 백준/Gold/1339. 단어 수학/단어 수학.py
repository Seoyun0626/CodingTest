# 한 원소안에 중복되는 알파벳이 존재하는 예외 사항 고려

import sys
input = sys.stdin.readline

n = int(input())
alpha = []
alpha_dic = {}
numList = [] # 수를 저장할 리스트
for _ in range(n):
    alpha.append(input().strip())
# print(alpha)

for i in range(len(alpha)):
    for j in range(len(alpha[i])):
        if alpha[i][j] in alpha_dic:
            alpha_dic[alpha[i][j]] += 10 ** (len(alpha[i]) - j - 1)
        else:
            alpha_dic[alpha[i][j]] = 10 ** (len(alpha[i]) - j - 1)
# print(alpha_dic)

for val in alpha_dic.values():
    numList.append(val)
numList.sort(reverse = True)

# print(numList)
sum = 0
num = 9

for i in numList:
    sum += num * i
    num -= 1
print(sum)