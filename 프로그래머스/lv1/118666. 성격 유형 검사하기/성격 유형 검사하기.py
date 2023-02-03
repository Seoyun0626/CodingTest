def solution(survey, choices):
    result = ""
    dic1 = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7:3}
    dic2 = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N":0}
    i = 0

    for x in choices:
        if x <= 3:
            index = survey[i][0]
            dic2[index] += dic1[x]
        elif x >=5 and x <=7:
            index = survey[i][1]
            dic2[index] += dic1[x]
        i += 1

    if dic2["R"] >= dic2["T"]:
        result += "R"
    else:
        result += "T"

    if dic2["C"] >= dic2["F"]:
        result += "C"
    else:
        result += "F"

    if dic2["J"] >= dic2["M"]:
        result += "J"
    else:
        result += "M"

    if dic2["A"] >= dic2["N"]:
        result += "A"
    else:
        result += "N"


    return result