def solution(maps):
    # 빨리 도착 -> 최단 거리 알고리즘 -> BFS

    from collections import deque

    # maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]] 
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # print(visited)

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
                    maps[ny][nx] = maps[y][x] + 1

    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n - 1][m - 1]