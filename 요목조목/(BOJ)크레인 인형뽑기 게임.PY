# 인덱스 비교 전에 비교 가능한 상태인지 확인 먼저 하기 (index 범위 초과 방지 위해)


board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 4, 0], [1, 2, 2, 1]]
moves = [2, 3, 1, 4, 2, 3]
stack = []
cnt = 0

for x in moves:
    for i in range(len(board)):
        if board[i][x - 1] != 0:
            stack.append(board[i][x - 1])
            board[i][x - 1] = 0
            break
    j = len(stack)
    while True:
        if j >= 2:
            if stack[j - 2] == stack[j - 1]:
                stack.pop()
                stack.pop()
                cnt += 2
                j -= 2
            else:
                break
        else:
            break
print(cnt)