n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
binary_arr1 = [[] * n for i in range(n)]
binary_arr2 = [[] * n for i in range(n)]
result = []

for i in range(len(arr1)):
    num = arr1[i]
    while True:
        if num != 0:
            binary_arr1[i].append(num % 2)
            num = num // 2
        else:
            break
for i in range(len(binary_arr1)):
    while len(binary_arr1[i]) != n:
        binary_arr1[i].append(0)
    binary_arr1[i] = binary_arr1[i][::-1]

for j in range(len(arr2)):
    num = arr2[j]
    while True:
        if num != 0:
            binary_arr2[j].append(num % 2)
            num = num // 2
        else:
            break
for i in range(len(binary_arr2)):
    while len(binary_arr2[i]) != n:
        binary_arr2[i].append(0)
    binary_arr2[i] = binary_arr2[i][::-1]

for i in range(n):
    string = ""
    for j in range(n):
        if binary_arr1[i][j] == 1 or binary_arr2[i][j] == 1:
            string += "#"
        else:
            string += " "
    result.append(string)
print(result)




