def solution(n, words):
    stack = []
    result = []
    flag = 0


    for i in range(len(words)):
        if len(stack) == 0:
            stack.append(words[i])
        else:
            if words[i] in stack:
                num = i
                flag = 1
                break
            else:
                pre = stack.pop()
                if pre[-1] != words[i][0]:
                    num = i
                    flag = 1
                    break
                else:
                    stack.append(pre)
                    stack.append(words[i])
    if flag == 0:
        result.append(0)
        result.append(0)
    else:
        result.append(num % n + 1)
        result.append(num // n + 1)

    return result