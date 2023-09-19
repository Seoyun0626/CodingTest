import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 1, -1, -1, 1, 0, 0]
def dfs(x, y):
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        graph = []
        cnt = 0
        for _ in range(h):
            line = list(map(int, input().split()))
            graph.append(line)
        # print(graph)
        for i in range(h):
            for j in range(w):
                if (graph[i][j] == 1):
                    dfs(i, j)
                    cnt += 1
        print(cnt)




