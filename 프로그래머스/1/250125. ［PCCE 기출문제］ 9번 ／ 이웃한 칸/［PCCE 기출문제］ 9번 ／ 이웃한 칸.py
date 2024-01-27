def solution(board, h, w):
    # 동 서 북 남
    direction = {0 : (0,1), 1 : (0,-1), 2 : (-1, 0), 3 : (1, 0)} 
    answer = 0
    color = board[h][w]
    for i in range(4):
        dx = w + direction[i][1]
        dy = h + direction[i][0]
        # print(dx,dy, board[dy][dx], color)
        if (0<=dx<=len(board[0])-1) and (0<=dy<=len(board)-1) and (board[dy][dx] == color):
            answer += 1
    return answer