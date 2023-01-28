price = 3
money= 20
count = 4


total = 0
for i in range(1, count + 1):
    total += price * i
result = total - money
print(result)