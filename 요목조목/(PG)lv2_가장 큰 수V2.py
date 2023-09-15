# 문자열 비교 -> 사전 순서처럼
numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]
# numbers = [0, 0, 0]

answer = ""
tmp = list(map(str, numbers))
tmp.sort(key=lambda x : x * 3, reverse=True)
print(tmp)

# 문자열 "000"방지를 위해 int로 떨군후 다시 str
answer =str(int("".join(tmp)))
print(answer)