def solution(sizes):
    result = 0
    big = []
    small = []


    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            big.append(sizes[i][0])
            small.append(sizes[i][1])
        else:
            big.append(sizes[i][1])
            small.append(sizes[i][0])

    result = max(big) * max(small)

    return result