# 숫자를 비교할 때 기준은 문자열 *3 왜냐? 310보다 3이 더 크게 작용 -> 자리 수 맞추기
# numbers의 모든 원소가 0 일 때 고려

# numbers = [6, 10, 2]
# numbers = [12, 121]
numbers= [0, 0, 0]
answer = ""
tmp = list(map(str, numbers))
# print(tmp)

tmp.sort(key = lambda x : x * 3, reverse = True)
# print(tmp)

answer = "".join(tmp)
answer = int(answer)
print(str(answer))

