input()
s = input()
hidden_numbers = []
is_number = False
num = ""
for i in s:
    if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if len(num) < 7 and len(num) != 0:
            hidden_numbers.append(int(num))
        num = ""
        continue
    num += i
if len(num) < 7 and len(num) != 0:
        hidden_numbers.append(int(num))
print(sum(hidden_numbers))