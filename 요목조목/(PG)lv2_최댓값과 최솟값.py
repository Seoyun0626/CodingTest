# s = "1 2 3 4"
s = "-1 -2 -3 -4"
s = "-1 -1"
answer = ""
tmp = list(map(int, s.split( )))
result = []
result.append(min(tmp))
result.append(max(tmp))
print(result)

for x in result:
    answer += str(x)
    answer += " "


print(answer.rstrip(" "))
