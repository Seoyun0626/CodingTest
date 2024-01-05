def solution(food):
    answer = ''
    tmp_answer = ''
    tmp = []
    for i in food:
        cnt = i//2
        tmp.append(cnt)
    for j in range(1,len(tmp)):
        num = j
        cnt = tmp[j]
        tmp_answer += str(num) * cnt
    reversed_tmp_answer = "".join(reversed(tmp_answer))
    answer = tmp_answer + "0" + reversed_tmp_answer
        
    return answer