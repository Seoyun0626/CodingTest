def solution(s, n):
    answer = ''
    big_dict = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    small_dict = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for word in s:
        if word in big_dict:
            cnt = (big_dict.index(word) + n) % 26
            answer += big_dict[cnt]
        elif word in small_dict:
            cnt = (small_dict.index(word) + n) % 26
            answer += small_dict[cnt]
        else:
            answer += " "
    return answer