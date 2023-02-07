# 연속된 숫자라고 대결하는 것이 아님

# N = 8
# A = 2
# B = 3
answer = 0
while True:
    if A + 1 == B and B % 2 == 0:
        break
    elif B + 1 == A and A % 2 == 0:
        break
    else:
        if A % 2 == 0:
            A = A // 2
        else:
            A = (A + 1) // 2
        if B % 2 == 0:
            B = B // 2
        else:
            B = (B + 1) // 2
    answer += 1
print(answer + 1)