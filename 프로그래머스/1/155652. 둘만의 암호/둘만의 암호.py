def solution(s, skip, index):
    answer = ''
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    store_index = index
    for word in s:
        word_index = alphabet.index(word)
        tmp = 1
        index = store_index
        # print(word_index)
        while tmp < (index+1):
            tmp_index = word_index + tmp
            if (tmp_index) > 25:
                tmp_index = (tmp_index) % 26
            if alphabet[tmp_index] not in skip:
                tmp += 1
                continue
            else:
                tmp += 1
                index += 1
        answer+=alphabet[tmp_index]
            
    return answer
print(solution("z", "abcdefghij", 20))