# hash 구조 -> set(key만 존재), dict(key, value 둘다 존재)
# input시 rstrip사용 -> "\n"삭제
# 문자열 in (리스트, 문자열, 딕셔너리..) -> 일부 일치 검사

import sys
input = sys.stdin.readline

check_dict = {}
cnt = 0
N, M = map(int, input().split())

for _ in range(N):
    key = input().rstrip()
    check_dict[key] = 0
# print(check_dict)

for _ in range(M):
    word = input().rstrip()
    if word in check_dict:
        cnt += 1
print(cnt)






