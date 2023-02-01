# 소수구하기는 에라토스테네스의 체 원리 사용이 효율적


num = [True] * (123456 * 2 + 1)



def prime():
    global j
    global num
    for i in range(2, 246913):
        if num[i] == True:
            j = 2
            while i * j <= 246912:
                if num[i * j] == True:
                    num[i * j] = False
                j += 1
prime()


arr = []
while True:
    value = int(input())
    if value != 0:
        arr.append(value)
    else:
        break



for i in range(len(arr)):
    x = arr[i]
    cnt = 0
    for j in range(x + 1, 2 * x + 1):
        if num[j] == True:
            cnt += 1
    print(cnt)



















# def prime(x):
#     if x == 1:
#         return False
#     else:
#         for i in range(2, int(math.sqrt(x)) + 1):
#             if x % i == 0:
#                 return False
#         return True
#
# for i in range(len(arr)):
#     x = arr[i]
#     cnt = 0
#     for j in range(x + 1, 2 * x + 1):
#         if prime(j):
#             cnt += 1
#     print(cnt)
