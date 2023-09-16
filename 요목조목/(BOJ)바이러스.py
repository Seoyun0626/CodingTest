n = int(input())
m = int(input())
cnt = 0
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
# print(graph)

def dfs(v):
    visited[v] = True
    for i in range(1, n + 1):
        if visited[i] == False and graph[v][i] == True:
            visited[i] = True
            dfs(i)

dfs(1)
print(sum(visited) - 1)


