def solution(s):
    answer = []
    dict = {}
    for i in range(len(s)):
        word = s[i]
        if word not in dict:
            dict[word] = i
            answer.append(-1)
        else:
            answer.append(i-dict[word])
            dict[word] = i
    return answer