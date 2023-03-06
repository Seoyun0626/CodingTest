# 풀이 참고

x = int(input())

line = 1
while x > line:
    x -= line
    line += 1

# line : 라인을 의미, x : 라인에서 몇 번째(1, 2, 3 ..)

if line % 2 == 1:
    down = x
    up = line + 1 - x
else:
    up = x
    down = line + 1 - x
result = str(up) + '/' + str(down)
print(result)

