dict = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
new_dict = {}
for k, v in dict.items():
    new_dict[v] = k

s = "23four5six7"
i = 0
result = []
string = ""
while i != len(s):
    string += s[i]
    print(string)
    if string in dict:
        result.append(int(string))
        i += 1
        string = ""
    else:
        if string in new_dict:
            result.append(int(new_dict[string]))
            i += 1
            string = ""
        else:
            i += 1
answer = ""
for x in result:
    answer += str(x)
print(answer)

# while i != len(s):
#     string = ""
#     for num, word in dict.items():
#         if s[i] == num:
#             result.append(int(s[i]))
#             i += 1
#             break
#         else:
#             while True:
#                 string += s[i]
#                 for num, word in dict.items():
#                     if string == word:
#                         result.append(int(num))
#                         print(i, result)
#                         break
#                 i += 1
















