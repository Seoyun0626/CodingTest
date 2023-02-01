def solution(dartResult):   
    # 넣다 뺴는 것 -> stack일 확률
    # 문자열 10을 숫자 10으로 인식하기 위해 replace 함수를 사용

    
    dic = {"S": 1, "D": 2, "T": 3}
    stack = []
    dartResult = dartResult.replace("10", "X")

    for x in dartResult:
        if x.isnumeric() or x == "X":
            if x == "X":
                stack.append(10)
            else:
                stack.append(int(x))
        elif x == "S" or x == "D" or x == "T":
            num = stack.pop()
            stack.append(pow(num, dic[x]))
        elif x == "*":
            if len(stack) == 1:
                num = stack.pop()
                stack.append(num * 2)
            else:
                num1 = stack.pop(-2)
                num2 = stack.pop()
                stack.append(num1 * 2)
                stack.append(num2 * 2)
        elif x == "#":
            num = stack.pop()
            stack.append(num * -1)
        
    answer = sum(stack)
    return answer