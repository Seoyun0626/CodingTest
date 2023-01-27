#맞지만 시간초과 난 코드

import sys
input = sys.stdin.readline


N = int(input())
num = []
absolute = []

def ft_print():
    if len(absolute) != 0:
        absolute.sort()
        ne_number = absolute[0] * -1
        po_number = absolute[0]
        if ne_number in num:
            print(ne_number)
            del absolute[0]
            num.remove(ne_number)
        elif po_number in num:
            print(po_number)
            del absolute[0]
            num.remove(po_number)
    else:
        print(0)


for _ in range(N):
    sign = int(input())
    if sign != 0:
        num.append(sign)
        absolute.append(abs(sign))
    else:
        ft_print()


