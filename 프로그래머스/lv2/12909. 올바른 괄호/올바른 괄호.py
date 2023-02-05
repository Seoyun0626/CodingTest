def solution(s):
    answer = True
    stack = []
    
    for x in s:
        if x == "(":
            stack.append(x)
        else:
            if len(stack) == 0:
                answer = False
                break
            else:
                stack.pop()
    if len(stack) > 0:
        answer = False 


    return answer