# dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31,8:31, 9:30, 10:31, 11:30, 12:31}
month, day = map(int, input().split())
month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answer = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
total = 0
for i in range(1, month):
    total += month_day[i]
total += day
total -= 1
result = total % 7
print(answer[result])

