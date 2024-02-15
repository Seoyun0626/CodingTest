def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        first = i // n
        second = i % n
        num = max(first, second)
        answer.append(num+1)
    return answer