d = [2,2,3,3]
budget = 10
cnt = 0


d.sort()

for i in range(len(d)):
    if budget // d[i] != 0:
        cnt += 1
        budget -= d[i]
    else:
        break
print(cnt)