def solution(wallpaper):
    left = []
    left_y = []
    left_x = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if (wallpaper[i][j] == "#"):
                left_y.append(i)
                left_x.append(j)
                left.append((i, j))
    right_y = []
    right_x = []
    for a,b in left:
        right_y.append(a+1)
        right_x.append(b+1)
    answer = []
    answer.append(min(left_y))
    answer.append(min(left_x))
    answer.append(max(right_y))
    answer.append(max(right_x))
    print(answer)
    return answer