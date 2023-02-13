T = int(input())
sec = [300, 60, 10]
result = []

if T // 300 != 0:
    result.append(T // 300)
    T = T % 300
else:
    result.append(0)
if T // 60 != 0:
    result.append(T // 60)
    T = T % 60
else:
    result.append(0)
if T // 10 != 0:
    result.append(T // 10)
    T = T % 10
else:
    result.append(0)
if T != 0:
    print("-1")
else:
    print(*result)
