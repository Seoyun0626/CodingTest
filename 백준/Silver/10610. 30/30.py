n = input()
num = []
for x in n:
    num.append(int(x))
num.sort(reverse= True)
# print(num)

if (sum(num) % 3 == 0) and ("0" in n):
    result = ""
    for x in num:
        print(x, end="")
else:
    print("-1")