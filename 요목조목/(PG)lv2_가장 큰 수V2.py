# 문자열 비교 -> 사전 순서처럼
# numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]
# numbers = [0, 0, 0]

answer = ""
# 문자열 비교일 때는 사전순으로 비교, int형 숫자가 크다고 해서 큰 것이 아님
tmp = list(map(str, numbers))
# numbers 원소는 0이상 1000이하 이므로 최소 *3은 해야지 비교 가능
tmp.sort(key=lambda x : x * 3, reverse=True)
# print(tmp)

# 문자열 "000"방지를 위해 int로 떨군후 다시 str
answer =str(int("".join(tmp)))
print(answer)