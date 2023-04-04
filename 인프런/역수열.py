n = int(input())
cnt = list(map(int, input().split()))
result = []
# print(cnt)
result = [0] * n
# print(result)
result[cnt[0]] = 1


def find(cur_cnt, num):
    total_cnt = 0
    for j in range(len(result)):
        if result[j] == 0:
            total_cnt += 1
        if total_cnt >= cur_cnt:
            tmp = j
            break
    if total_cnt > cur_cnt:
        result[tmp] = num
    else:
        for k in range(tmp + 1, len(result)):
            if result[k] == 0:
                result[k] = num
                break



for i in range(1, len(cnt)):
    cur_cnt = cnt[i]
    num = i + 1
    find(cur_cnt,num)
    # print(result)
print(*result)