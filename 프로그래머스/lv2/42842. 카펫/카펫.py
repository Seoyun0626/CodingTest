def solution(brown, yellow):
    import math

    # brown = 10
    # yellow = 2
    # brown = 8
    # yellow = 1
    # brown = 24
    # yellow = 24
    total = brown + yellow
    # t_cnt = math.sqrt(total)
    # y_cnt = math.sqrt(yellow)
    # print(t_cnt, y_cnt)
    t_arr = []
    y_arr = []
    result = []

    for i in range(total, 0, -1):
        num = total // i
        if total % i == 0 and num <= i:
            t_arr.append((i, num))
    # print(t_arr)

    for i in range(yellow, 0, -1):
        num = yellow // i
        if yellow % i == 0 and num <= i:
            y_arr.append((i, num))
    # print(y_arr)

    for i in range(len(y_arr)):
        x = y_arr[i][0]
        y = y_arr[i][1]
        if (x+2, y+2) in t_arr:
            result.append(x + 2)
            result.append(y + 2)
            break

    return result