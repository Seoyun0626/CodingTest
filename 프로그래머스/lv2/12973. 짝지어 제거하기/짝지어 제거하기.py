def solution(s):
    # 문자열의 길이가 넘 크면 시간 초과
    # 전에 들어온 것들과 비교 -> stack활용

    # s = "baabaa"
    i = 0
    # s = "cdcd"
    stack = []

    for x in s:
        if len(stack) == 0:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)

    if len(stack) == 0:
        answer = 1
    else:
        answer = 0



    return answer