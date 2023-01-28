#바로 직전과 비교 -> stack 자료구조 또는 list 사용

arr = [1, 1, 3, 3, 0, 1, 1]
stack = []
for i in range(len(arr)):
    if len(stack) == 0:
        stack.append(arr[0])
    else:
        if stack[-1] == arr[i]:
            continue
        else:
            stack.append(arr[i])
print(stack)



