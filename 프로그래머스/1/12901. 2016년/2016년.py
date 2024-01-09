def solution(a, b):
    answer = ''
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU",]
    cnt = 0
    months = months[0:a-1]
    print(months)
    cnt = (sum(months) + b)
    real_day = cnt % 7
    answer += day[real_day - 1]
    return answer