def solution(board, moves):

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

    return cnt