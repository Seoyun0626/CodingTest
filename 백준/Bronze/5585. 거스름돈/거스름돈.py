import sys

input = sys.stdin.readline
money = int(input())
cnt = 0

money = 1000 - money

if (money // 500) != 0:
    cnt += money // 500
    money = money - (money // 500) * 500
# print(money, cnt)
if (money // 100) != 0:
    cnt += money // 100
    money = money - (money // 100) * 100
# print(money, cnt)
if (money // 50) != 0:
    cnt += money // 50
    money = money - (money // 50) * 50
# print(money, cnt)
if (money // 10) != 0:
    cnt += money // 10
    money = money - (money // 10) * 10
# print(money, cnt)
if (money // 5) != 0:
    cnt += money // 5
    money = money - (money // 5) * 5
# print(money, cnt)

cnt += money

print(cnt)
