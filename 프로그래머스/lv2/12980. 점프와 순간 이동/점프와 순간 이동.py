def solution(N):
    # N = 5000
    # N = 5
    # N = 6
    result = 0


    while N != 0:
        if N % 2 == 0:
            N = N // 2
        else:
            result += 1
            N = N // 2


    return result