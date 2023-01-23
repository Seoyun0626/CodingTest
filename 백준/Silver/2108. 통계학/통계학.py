#딕셔너리 잘 사용하기


import sys
input = sys.stdin.readline


def first_command():
    average = sum(num) / len(num)
    if (abs(average) == 0):
        print("0")
    else:
        print(round(average))

def second_command():
    num.sort()
    print(num[len(num) // 2])


def third_command():
    my_dict = {}
    for x in num:
        if x in my_dict:
            my_dict[x] += 1
        else:
            my_dict[x] = 1
    new_dict = sorted(my_dict.items(), key=lambda x : (x[1], x[0]), reverse=True)
    cnt = 1
    big = new_dict[0][1]
    result = []
    result.append(new_dict[0][0])
    for i in range(1, len(new_dict)):
        if new_dict[i][1] == big:
            cnt += 1
            result.append(new_dict[i][0])
    if cnt == 1:
        print(result[0])
    else:
        print(result[-2])


def fourth_command():
    print(max(num) - min(num))




N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

first_command()
second_command()
third_command()
fourth_command()

