def solution(babbling):
    answer = 0
    baby_word = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        flag = 1
        while flag == 1:
            if word[0:3] == "aya":
                if word[3:6] == "aya":
                    break
                word = word[3:]
                continue
            elif word[0:2] == "ye":
                if word[2:4] == "ye":
                    break
                word = word[2:]
                continue
            elif word[0:3] == "woo":
                if word[3:6] == "woo":
                    break
                word = word[3:]
                continue
            elif word[0:2] == "ma":
                if word[2:4] == "ma":
                    break
                word = word[2:]
                continue
            else:
                flag = 0
        if len(word) == 0:
            answer += 1
    return answer