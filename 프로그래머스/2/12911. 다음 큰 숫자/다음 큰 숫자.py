# 2진수 변환 후 1의 개수 계산하는 함수
def count(num):
    binary = bin(num)
    binary = binary[2:] # bin 함수 사용으로 인한 문자열 0b제거
    # print(binary)
    one = binary.count("1")
    return one
def solution(n):
    answer = n
    while True:
        answer += 1
        if count(answer) == count(n):
            break
    return answer