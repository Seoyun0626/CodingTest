# 인접 행렬, stack 자료 구조

## 인접 행렬 생성
n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[b][a] = matrix[a][b] = 1

## dfs 함수
def dfs(matrix, i, visited):
    stack = [i]
    while stack:
        value = stack.pop()
        if not visited[value]:
            print(value, end=" ")
            visited[value] = True
        ### 이미 방문 했던 지점 -> 바로 전 지점에서 방문하지 않는 지점 확인
        for c in range(len(matrix[value] - 1), -1, -1):
            if matrix[value][c] == 1 and not visited[c]:
                stack.append(c)
dfs(matrix, v, visited)


# 인접 행렬, 재귀함수 구조

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[b][a] = matrix[a][b] = 1

def dfs(matrix, i, visited):
    visited[i] = True
    print(i, end=" ")
    for c in range(len(matrix[i])):
        ### 정보가 방문한 곳일 수도 있고 아닐 수도 있으므로 1체크
        if matrix[i][c] == 1 and not visited[i]:
            dfs(matrix, c, visited)
dfs(matrix,v, visited)

# 인접 리스트, stack 자료 구조

## 인접 리스트 : 이중 list 구현
## 인접 행렬에서는 모든 행을 반복문으로 확인해 연결정보를 얻었음, graph[value]한번 만으로 모든 연결정보

n, m, v = map(int, input().split())
graph = [[]] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    if graph[a] == []:
        graph[a] = b
    else:
        graph[a].append(b)
    if graph[b] == []:
        graph[b] = a
    else:
        graph[b].append(a)

def dfs(graph, i, visited):
    stack = [i]
    visited[i] = True
    while stack:
        value = stack.pop()
        if not visited[value]:
            print(value, end=" ")
            visited[value] = True
        for j in graph[value]:
            ### 정보들은 다 방문한 곳들 -> 1체크할 필요 없음
            if not visited[j]:
                stack.append(j)
for i in graph:
    i.reverse()
dfs(graph, v, visited)

# 인접 리스트 재귀함수

n, m, v = map(int, input().split())
graph = [[]] * (n + 1)
visited[False] = (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    if graph[a] == []:
        graph[a] = b
    else:
        graph[a].append(b)
    if graph[b] == []:
        graph[b] = a
    else:
        graph[b].append(a)

def dfs(graph, i, visited):
    visited[i] = True
    print(i, end=" ")
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, j, visited)
dfs(graph, v, visited)

# =========================== BFS ====================================== #

# 인접행렬, queue 자료구조

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

from collections import deque

def bfs(matrix, i, visited):
    deque = deque()
    deque.append(i)
    while queue:
        value = queue.popleft()
        if not visited[value]:
            visited[value] = True
            print(value, end=' ')
        for c in range(len(matrix[value])):
            if matrix[value][c] == 1 and not visited[c]:
                queue.append(c)
# 인접리스트, queue 자료 구조

n, m, v = map(int, input().split())
graph = [[]] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    if graph[a] == []:
        graph[a] = b
    else:
        graph[a].append(b)
    if graph[b] == []:
        graph[b] = a
    else:
        graph[b].append(a)
from collections import deque

def bfs(graph, i, visited):
    queue = deque()
    queue.append(i)
    while queue:
        value = queue.popleft()

        if not visited[value]:
            print(value, end=" ")
            visited[value] = True
        for j in graph[value]:
            queue.append(j)
bfs(graph, v, visited)

