endNumList = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6],
              [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]


def sol(base, expo):
    baseEndNum = base % 10
    expoEndNum = expo % len(endNumList[baseEndNum])
    return endNumList[baseEndNum][expoEndNum - 1]


for i in range(int(input())):
    a, b = map(int, input().split())
    print(sol(a, b))