N = int(input())
check = 666
count = 0

while True:
    if "666" in str(check):
        count += 1
    if count == N:
        print(check)
        break
    check += 1



