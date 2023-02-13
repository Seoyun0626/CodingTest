n = int(input())
string = input()
result = 0
i = 0
while i != n:
    if string[i].isalpha():
        i += 1
    else:
        num = ""
        while string[i].isnumeric():
            num += string[i]
            i += 1
            if i == len(string):
                break
        result += int(num)
print(result)



