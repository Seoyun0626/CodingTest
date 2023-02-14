n = 437674
k = 3
# n = 110011
# k = 10
num = ""
def is_prime(check):
    if check == 1:
        return 0
    for i in range(2, (int(check ** (1 / 2) + 1))):
        if check % i == 0:
            return 0
    return 1

while n != 0:
    num += str(n % k)
    n = n // k

num = num[::-1]
# print(num)

i = 0
arr= []
while i != len(num):
    tmp = ""
    while num[i] != "0":
        tmp += num[i]
        i += 1
        if i == len(num):
            break
    # print(i, len(str))
    if len(tmp):
        arr.append(int(tmp))
    else:
        i += 1
# print(arr)

result = 0
for x in arr:
    if is_prime(x):
        result += 1
print(result)



