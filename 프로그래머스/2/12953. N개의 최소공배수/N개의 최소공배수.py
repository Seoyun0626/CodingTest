def solution(arr):
    answer = 0
    for _ in range(len(arr)-1):
        a = arr.pop(0)
        b = arr.pop(0)
        # print(a,b)
        for i in range(max(a,b), a*b+1):
            if i%a == 0 and i%b == 0:
                arr.append(i)
                break
    answer = arr[0]
    return answer
        