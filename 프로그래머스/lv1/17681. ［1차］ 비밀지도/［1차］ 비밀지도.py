def solution(n, arr1, arr2):
    binary_arr1 = [[] * n for i in range(n)]
    binary_arr2 = [[] * n for i in range(n)]
    result = []

    for i in range(n):
        num = arr1[i]
        while True:
            if num != 0:
                binary_arr1[i].append(num % 2)
                num = num // 2
            else:
                break
    for i in range(n):
        while len(binary_arr1[i]) != n:
            binary_arr1[i].append(0)
        binary_arr1[i] = binary_arr1[i][::-1]

    for j in range(n):
        num = arr2[j]
        while True:
            if num != 0:
                binary_arr2[j].append(num % 2)
                num = num // 2
            else:
                break
    for i in range(n):
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
    return result