import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
cnt = 0
n, m = map(int,input().split())
visited = [False] * (n + 1)
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
# print(graph)

def dfs(index):
    global cnt
    visited[index] = True
    for i in range(len(graph[index])):
        if graph[index][i] == 1 and not visited[i] :
            dfs(i)
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)

