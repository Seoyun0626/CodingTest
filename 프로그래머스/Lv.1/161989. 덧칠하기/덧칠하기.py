def solution(n, m, section):
    answer = 0
    paint = 0 #이 번호까지는 칠해짐
    for num in section:
        # print(num, paint)
        if num > paint:
            paint = (num+m-1)
            answer += 1
            # print(num,paint)
            
    return answer