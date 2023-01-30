#큰 것들 중에서 큰 것 + 작은 것들 중에서 큰 것


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
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
print(result)

