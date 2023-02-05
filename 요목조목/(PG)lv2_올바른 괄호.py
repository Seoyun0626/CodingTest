s = ")()("
stack = []

for x in s:
    if x == "(":
        stack.append(x)
    else:
        if len(stack) == 0:
            answer = "false"
            break
        else:
            stack.pop()
if len(stack) > 0:
    answer = "false"
print(answer)

