def solution(k, score):
    answer = []
    score_set = []
    for i in range(len(score)):
        tmp_score = score[i]
        if (i<k):
            score_set.append(tmp_score)
            score_set.sort(reverse=True)
            answer.append(score_set[-1])
        else:
            score_set.append(tmp_score)
            score_set.sort(reverse=True)
            answer.append(score_set[k-1])
    # print(answer)
    return answer