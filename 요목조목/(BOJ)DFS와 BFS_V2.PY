# DFS(재귀 함수)6

from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
d_visited = [False] * (n + 1)
b_visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
# print(graph)
# print(visited)

def dfs(v):
    d_visited[v] = True
    print(v, end=" ")
    for i in range(1, n + 1):
        if d_visited[i] == False and graph[v][i] == True:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    b_visited[v] = True
    while queue:
        value = queue.popleft()
        print(value, end=" ")
        for i in range(1, n + 1):
            if (b_visited[i] == False) and (graph[value][i] == True):
                queue.append(i)
                b_visited[i] = 1
        # print(queue)

dfs(v)
print()
# print(graph)
bfs(v)
