# n = 3
# words =["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# n = 5
# words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
# n = 2
# words = ["hello", "one", "even", "never", "now", "world", "draw"]
stack = []
result = []
flag = 0


for i in range(len(words)):
    print(stack, words[i])
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
print(i)
if flag == 0:
    result.append(0)
    result.append(0)
else:
    result.append(num % n + 1)
    result.append(num // n + 1)
print(result)




