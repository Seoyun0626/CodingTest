
# N * M 얼음틀(2차원 배열) 구멍:0 칸막기:1 => 생성되는 아이스크림의 수
# 2차원 배열에서 0,1을 탐색을 통해 아이스크림수 구하기 -> DFS,BFS사용이지 않을까??

def dfs(graph, x, y):
    if (x < 0 or y < 0 or x >= N or y >= M):
        return False
    if (graph[x][y] == 0):
        graph[x][y] = 1
        dfs(graph, x - 1, y)
        dfs(graph, x + 1, y)
        dfs(graph, x, y - 1)
        dfs(graph, x, y + 1)
        return True
    else:
        return False

N, M = list(map(int, input().split()))
ICE = []
for _ in range(N):
    ICE.append(list(map(int, input())))


cnt = 0
for i in range(N):
    for j in range(M):
        if (dfs(ICE, i, j) == True):
            cnt += 1                 
print(cnt)

