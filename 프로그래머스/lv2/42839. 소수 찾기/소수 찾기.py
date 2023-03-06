def solution(numbers):
    from itertools import permutations
    import math
    # numbers = "011"
    arr = [n for n in numbers]
    # print(arr)
    answer = []
    def is_prime(x):
        cnt = 0
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                cnt += 1
        if cnt == 0:
            answer.append(x)

    num_arr = []
    tmp = []
    for j in range(1,len(numbers) + 1):
        tmp += list(permutations(arr, j))
    num_arr = [int(("").join(p)) for p in tmp]
    num_arr = list(set(num_arr))
    # print(num_arr)

    for x in num_arr:
        if x != 1 and x != 0:
            is_prime(x)
    # print(answer)






    return len(answer)