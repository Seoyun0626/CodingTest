def solution(numbers):
    # 문자열 비교 -> 사전 순서처럼
    # numbers = [6, 10, 2]
    # numbers = [3, 30, 34, 5, 9]

    answer = ""
    tmp = list(map(str, numbers))
    tmp.sort(key=lambda x : x * 3, reverse=True)
    # print(tmp)

    answer =str(int("".join(tmp)))
    return answer