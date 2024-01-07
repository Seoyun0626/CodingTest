def solution(strings, n):
    answer = []
    strings = sorted(strings)
    answer = sorted(strings, key = lambda x : x[n])
    return answer