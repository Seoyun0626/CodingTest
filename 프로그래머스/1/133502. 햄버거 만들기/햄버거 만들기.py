def solution(ingredient):
    tmp = []
    answer = 0
    for i in ingredient:
        tmp.append(i)
        if (tmp[-4:] == [1,2,3,1]):
            del tmp[-4:]
            answer+=1
    return answer