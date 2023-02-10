n = int(input())
cnt = 0



for _ in range(n):
    word = input()
    dic = {}
    flag = 0
    for i in range(len(word)):
        if word[i] not in dic:
            dic[word[i]] = 1
        else:
            if word[i] == word[i - 1]:
                continue
            else:
                flag = 1
                break
        # print(dic)
    if flag == 0:
        cnt += 1
print(cnt)