word = "a, e, i, o, u"
n = input()
cnt = 0
for x in n:
    if x in word:
        cnt += 1
print(cnt)