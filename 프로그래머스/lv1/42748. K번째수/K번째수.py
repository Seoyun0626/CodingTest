def solution(array, command):
    result = []

    for i in range(len(command)):
        num = array[command[i][0] - 1:command[i][1]]
        num.sort()
        final = num[command[i][2] - 1]
        result.append(final)

    return result