def solution(k, dungeons):
    # 순열을 이용
    # 순열을 이용

    from itertools import permutations

    # k = 80
    # dungeons = [[80, 20], [80, 10], [70, 20], [50, 40], [10, 10]]
    # k = 100
    # dungeons = [[80, 8], [90, 9], [100, 10]]
    result = []

    for permut in permutations(dungeons, len(dungeons)):
        # print(permut)
        cnt = 0
        cur = k
        for a,b in permut:
            # print(cur, a, b)
            if cur < a:
                break
            else:
                cur = cur - b
                cnt += 1
            result.append(cnt)
    answer = max(result)



    return answer