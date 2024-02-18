def solution(s):
    answer = 0
    tmp = list(s)
    result = check(tmp)
    if result == 1:
        answer += 1
    for x in range(1,len(s)):
        tmp.append(tmp.pop(0)) 
        result = check(tmp)
        if result == 1:
            answer += 1
    return answer
def check(x):
    stack = []
    for i in x:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)
    # print(x, len(stack))
    if len(stack) == 0:
        return 1
    else:
        return -1
        
            
            
        