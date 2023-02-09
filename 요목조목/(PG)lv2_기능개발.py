from collections import deque


# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
queue = deque()
result = []

for i in range(len(progresses)):
    if (100 - progresses[i]) % speeds[i] == 0:
        queue.append((100 - progresses[i]) // speeds[i])
    else:
        queue.append((100 - progresses[i]) // speeds[i] + 1)

while len(queue) != 0:
    if len(queue) == 1:
        result.append(1)
        break
    else:
        print(queue, result)
        cnt = 1
        standard = queue.popleft()
        while len(queue) != 0:
            num = queue.popleft()
            print(standard, num)
            if standard >= num:
                cnt += 1
            else:
                queue.appendleft(num)
                break
        result.append(cnt)
print(result)






