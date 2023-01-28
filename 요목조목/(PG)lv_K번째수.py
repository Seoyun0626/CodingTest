array = [1, 5, 2, 6, 3, 7, 4]
command= [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
i = 2
j = 5
k = 3
result = []
for i in range(len(command)):
    num = array[command[i][0] - 1:command[i][1]]
    num.sort()
    final = num[command[i][2] - 1]
    result.append(final)
print(result)
