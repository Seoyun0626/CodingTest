from string import ascii_uppercase

def solution(msg):
    answer = []
    dict = {}
    index = 1
    for i in ascii_uppercase:
        dict[i] = index
        index += 1
    # print(dict)
    idx = 0
    while True:
        word = ""
        word += msg[idx]
        idx += 1
        if idx == len(msg):
            answer.append(dict[word])
            break
        while True:
            if word in dict:
                tmp = dict[word]
                word += msg[idx]
                idx += 1
                if idx == len(msg) and word in dict:
                    answer.append(dict[word])
                    break
                elif idx == len(msg) and word not in dict:
                    answer.append(tmp)
                    idx -= 1
                    break
            else:
                dict[word] = index
                index += 1
                answer.append(tmp)
                idx -= 1
                break
        if idx == len(msg):
            break
                
    return answer