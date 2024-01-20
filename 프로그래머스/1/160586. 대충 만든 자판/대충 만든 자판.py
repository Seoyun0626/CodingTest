def solution(keymap, targets):
    answer = []
    dict = {}
    for i in range(len(keymap)):
        word = keymap[i]
        for j in range(len(word)):
            key = word[j]
            if key not in dict:
                dict[key] = j+1
            else:
                tmp = dict[key]
                if (j+1) < tmp:
                    dict[key] = j+1
    for i in range(len(targets)):
        word = targets[i]
        cnt = 0
        flag = 0 
        for j in range(len(word)):
            if word[j] in dict:
                cnt += dict[word[j]]
            else:
                flag = 1
                break
        if flag == 1:
            answer.append(-1)
        else:
            answer.append(cnt)
    return answer