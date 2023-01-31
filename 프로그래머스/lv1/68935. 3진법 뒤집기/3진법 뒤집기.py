def solution(n):
    string = ""
    while (n != 0):
        string += str(n % 3)
        n = n // 3
    result = 0
    string = string[::-1]

    for i in range(len(string)):
        result += (3 ** i) * int(string[i])
    return result