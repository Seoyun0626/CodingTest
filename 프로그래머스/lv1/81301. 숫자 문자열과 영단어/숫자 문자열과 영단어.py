def solution(s):
    dict = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    new_dict = {}
    for k, v in dict.items():
        new_dict[v] = k


    i = 0
    result = []
    string = ""
    while i != len(s):
        string += s[i]
        if string in dict:
            result.append(int(string))
            i += 1
            string = ""
        else:
            if string in new_dict:
                result.append(int(new_dict[string]))
                i += 1
                string = ""
            else:
                i += 1
    answer = 0
    for x in result:
        answer = answer * 10 + x
    return answer