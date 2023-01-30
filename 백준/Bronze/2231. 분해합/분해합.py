# map함수 잘 활용하기
import sys
input = sys.stdin.readline
N = int(input())
num = 0
flag = 0

for i in range(1, N + 1):
    each_num = sum(map(int, str(i))) #각 자리수를 더하기 위해 str사용 후 sum함수 계산을 위해 int형으로 바꾸기
    num = i + each_num
    if num == N:
        print(i)
        flag = 1
        break
if flag == 0:
    print("0")






