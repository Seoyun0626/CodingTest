n = int(input())
result = []
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(n):
    graph.append(list(map(int, input())))
# print(graph)

def dfs(x, y):
    # 예외 사항 처리
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0 # 이미 지나갔다고 표시하기 위해
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

count = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result.append(count)
            count = 0
result.sort()
print(len(result))
for num in result:
    print(num)


