def solution(s):
    # s = "3people unFollowed  me   w"
    result = ""
    i = 0
    flag = 0
    while True:
        # print(s[i], len(s))
        if s[i].islower():
            result += s[i].upper()
        else:
            result += s[i]
        i += 1
        # print(result, s[i], i, len(s))
        if i == len(s):
            # print(result)
            break
        while s[i] != " ":
            if s[i].isupper():
                result += s[i].lower()
            else:
                result += s[i]
            i += 1
            if i == len(s):
                flag = 1
                break
            # print(result, i, s[i], flag, len(s))
        if flag == 1:
            # print(result)
            break
        # print(result)
        # print(result, i, s[i], len(s))
        while s[i] == " ":
            result += s[i]
            i += 1
            if len(s) == i:
                flag = 1
                break
        if flag == 1:
            # print(result)
            break
    return result