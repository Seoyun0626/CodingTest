# 다중 교집합, 다중 합집합

import math

# str1 = "FRANCE"
# str2 = "french"
# str1 = "E=M*C^2"
# str2 = "e=m*c^2"
# str1 = "aa1+aa2"
# str2 = "AAAA12"
# str1 = "handshake"
# str2 = "shake hands"
arr1 = []
arr2 = []
result = 0

str1 = str1.upper()
str2 = str2.upper()

i = 0
while i + 1 < len(str1):
    string = str1[i] + str1[i + 1]
    arr1.append(string)
    i += 1
# print(arr1)

j = 0
while j + 1 < len(str2):
    string = str2[j] + str2[j + 1]
    arr2.append(string)
    j += 1
# print(arr2)

i = 0
while i != len(arr1):
    # print(arr1[i][0], arr1[i][1])
    if arr1[i][0].isalpha() and arr1[i][1].isalpha():
        i += 1
    else:
        arr1.remove(arr1[i])
print(arr1)

j = 0
while j != len(arr2):
    if arr2[j][0].isalpha() and arr2[j][1].isalpha():
        j += 1
    else:
        arr2.remove(arr2[j])
print(arr2)

if len(arr1) == 0 and len(arr2) == 0:
    result = 1
elif (len(arr1) != 0 and len(arr2) == 0) or (len(arr1) == 0 and len(arr2) != 0):
    result = 0
else:
    tmp1 = []
    arr1_temp = arr1.copy()
    tmp2 = arr1.copy()

    for j in arr2:
        if j not in arr1_temp:
            tmp2.append(j)
        else:
            arr1_temp.remove(j)
    print(tmp2)

    for i in arr2:
        if i in arr1:
            arr1.remove(i)
            tmp1.append(i)
    print(tmp1)

    result = len(tmp1) / len(tmp2)
result = math.trunc(result * 65536)
print(result)





