# graph가 x,y좌표일 때 dfs인수 x,y
# x == m, y == n, 2차원 배열 앞부분 열(y), 뒷부분 행(n)
# 런타임 에러 : 최대 깊이를 초과하여 재귀 호출 -> 최대 깊이 늘려주기
import sys
sys.setrecursionlimit(10000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
t = int(input())

def dfs(x, y):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == 1:
                # 이미 지나간 것을 표시
                graph[ny][nx] = -1
                dfs(nx, ny)

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    # print(graph)
    for _ in range(k):
        a, b = map(int, input().split())
        # 가로, 세로와 X축 Y축은 반대
        graph[b][a] = 1
    # print(graph)
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)



