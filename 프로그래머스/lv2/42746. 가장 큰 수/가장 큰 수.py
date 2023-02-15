def solution(numbers):
    # 숫자를 비교할 때 기준은 문자열 *3 왜냐? 310보다 3이 더 크게 작용 -> 자리 수 맞추기

    # numbers = [6, 10, 2]
    answer = ""
    tmp = list(map(str, numbers))
    # print(tmp)

    tmp.sort(key = lambda x : x * 3, reverse = True)
    # print(tmp)

    answer = "".join(tmp)
    answer = int(answer) #[0,0,0] 일때 000출력 방지
    answer = str(answer)

    return answer