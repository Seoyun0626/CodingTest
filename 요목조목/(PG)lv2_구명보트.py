# 변수선언 초기화 잘 확인
# remove,del함수 사용 -> 시간초과 날 수 있음

people = [70, 50, 80, 50]
# people = [70, 80, 50]
# people = [50]
# people = [80, 70, 50, 20, 10]
limit = 100
cnt = 0
start_index = 0
last_index = len(people) - 1
people.sort()

while start_index <= last_index:
    if people[start_index] + people[last_index] > limit:
        last_index -= 1
    else:
        start_index += 1
        last_index -= 1
    cnt += 1
print(cnt)
