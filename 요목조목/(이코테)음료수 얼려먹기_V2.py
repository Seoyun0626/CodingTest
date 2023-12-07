n, m = map(int, input().split())
graph = []
cnt = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(n):
    line = list(map(int, input()))
    graph.append(line)
# print(graph)

def dfs(x, y):
    if 0 > x or x <= n or 0 > y or y <= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x - 1, y - 1)
        dfs(x, y - 1)
        dfs(x, y)
        return True
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1
print(cnt)
