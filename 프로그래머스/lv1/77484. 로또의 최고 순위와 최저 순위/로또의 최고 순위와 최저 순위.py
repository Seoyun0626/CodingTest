def solution(lottos, win_nums):
    check = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    result = []


    cnt = 0
    win_cnt = 0
    lose_cnt = 0
    zero_cnt = 0

    for x in lottos:
        for y in win_nums:
            if x == y:
                cnt += 1
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero_cnt += 1

    win_cnt = zero_cnt + cnt
    lose_cnt = cnt

    result.append(check[win_cnt])
    result.append(check[lose_cnt])

    return result