# flag는 멈출 때 사용

while True:
    s = input()
    flag = 0
    stack = []

    if s == ".":
        break

    for i in s:
        if i == "[" or i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) != 0:
                if stack.pop() == "(":
                    flag = 0
                else:
                    flag = 1
                    print("no")
                    break
            else:
                print("no")
                flag = 1
                break
        elif i == "]":
            if len(stack) != 0:
                if stack.pop() == "[":
                    flag = 0
                else:
                    print("no")
                    flag = 1
                    break
            else:
                print("no")
                flag = 1
                break
    if flag == 0:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")
