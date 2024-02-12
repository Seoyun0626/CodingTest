def solution(elements):
    answer = []
    for i in range(1, len(elements)+1):
        length = i
        for idx in range(len(elements)):
            if i+idx < len(elements):
                answer.append(sum(elements[idx:idx+i]))
            else:
                answer.append(sum(elements[idx:])+sum(elements[:idx+i-len(elements)]))
    # answer = len(list(set(answer)))
    # print(answer)
    answer = len(set(answer))
    return answer