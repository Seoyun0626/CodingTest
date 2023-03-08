from itertools import combinations
import sys
input = sys.stdin.readline


result = []
L, C = map(int, input().split())
word = list(map(str, input().split()))
word = sorted(word)
vowels = ["a", "e", "i", "o", "u"]

check = combinations(word, L)
check = list(check)
# print(check)
result = []




for i in range(len(check)):
    num = 0
    tmp = ""
    for x in check[i]:
        tmp += x
        if x in vowels:
            num += 1
    if num >= 1 and L - num >= 2:
        result.append(tmp)
for x in result:
    print(x)

