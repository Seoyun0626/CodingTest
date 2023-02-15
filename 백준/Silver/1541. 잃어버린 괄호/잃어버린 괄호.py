import sys

input = sys.stdin.readline
s = input()
arr = []
result = 0
string = ""
for i in range(len(s)):
    if s[i] != "-" and s[i] != "+":
        string += s[i]
    else:
        arr.append(string)
        arr.append(s[i])
        string = ""
arr.append(string.strip("\n"))
# print(arr)
flag = 0
i = 0
while True:
    if arr[i].isnumeric():
        result += int(arr[i])
    elif arr[i] == "-":
        i += 1
        while arr[i] != "-":
            if arr[i].isnumeric():
                result -= int(arr[i])
            i += 1
            if i == len(arr):
                flag = 1
                break
        i -= 1
    if flag:
        break
    i += 1
    if len(arr) == i:
        break
print(result)


