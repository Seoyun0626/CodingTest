# 정렬을 할 때 sorted, sort를 사용하는 경우 -> 중복되는 값에 대해서 원래 순서와 달라지는 불안정한 정렬 발생 가능X


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# files = ["a0","a1"]
tmp = []
for x in files:
    HEAD = ""
    NUMBER = ""
    TAIL = ""
    i = 0
    while True:
        if x[i].isnumeric():
            break
        else:
            HEAD += x[i]
            i += 1
    while x[i].isnumeric():
        NUMBER += x[i]
        i += 1
        if i == len(x):
            break
    while i != len(x):
        TAIL += x[i]
        i += 1
    tmp.append((HEAD, NUMBER, TAIL))
print(tmp)

tmp = sorted(tmp, key = lambda x : (x[0].lower(), int(x[1])))

# print("결과")
# print(result)
answer = [''.join(i) for i in tmp]
print(answer)
