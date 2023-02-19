from collections import deque

# priorities = [2, 1, 3, 2]
# location = 2
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
queue = deque() #초기 순서, 중요도
result = {}
find_index = 1
for i in range(len(priorities)):
    queue.append((i, priorities[i]))
print(queue)

while queue:
    flag = 0
    check = queue.popleft()
    num, importance = check[0], check[1]
    for i in range(len(queue)):
        if importance < queue[i][1]:
            flag = 1
            break
    if flag == 0:
        result[num] = find_index
        find_index += 1
    else:
        queue.append((num,importance))
print(result)
print(result[location])





