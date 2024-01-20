def solution(s):
    answer = 0
    idx = 0
    while idx != len(s):
        x = s[idx]
        x_cnt = 1
        y_cnt = 0
        idx += 1
        if idx == len(s):
            answer += 1
            break
        while x_cnt != y_cnt:
            if idx == len(s):
                break
            if s[idx] == x:
                x_cnt += 1
                idx += 1
            else:
                y_cnt += 1
                idx += 1
        answer += 1
        # print(idx)
    return answer