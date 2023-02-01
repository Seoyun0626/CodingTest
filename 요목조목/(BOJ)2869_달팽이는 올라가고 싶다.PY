# ..

A, B, V = map(int, input().split())
check = (V - B) / (A - B)

if check == int(check):
    print(int(check))
else:
    print(int(check) + 1)
