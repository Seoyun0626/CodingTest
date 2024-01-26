def solution(park, routes):

    x, y = 0, 0  # 시작점
    w, h = len(park[0]), len(park)  # 가로, 세로
    op = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    
    # 시작점
    for i in range(h):
        for j in range(w):
            if park[i][j]=="S":
                x, y = i, j
                break
        
    # 좌표이동
    for r in routes:
        d, n = r.split(" ") # 방향, 이동횟수
        dx, dy = x, y  # 현재위치
        
        for i in range(int(n)):
            # 이동할 위치
            nx = x + op[d][0]
            ny = y + op[d][1]
        
            if 0<=nx<=h-1 and 0<=ny<=w-1 and (park[nx][ny]!="X"):
                x, y = nx, ny
                    
            else:
                x, y = dx, dy
                break

    return (x,y)