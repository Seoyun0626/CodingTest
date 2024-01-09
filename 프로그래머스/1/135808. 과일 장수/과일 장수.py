def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    # print(score)
    for i in range(m-1, len(score), m):
        answer += score[i] * m
    return answer