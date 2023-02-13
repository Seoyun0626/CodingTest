a, b = map(str, input().split())
big = []
small = []
result = []

small_a = ""
small_b = ""
big_a = ""
big_b = ""
if "6" in a:
    small_a = a.replace("6", "5")
    small.append(int(small_a))
else:
    small.append(int(a))
if "6" in b:
    small_b = b.replace("6", "5")
    small.append(int(small_b))
else:
    small.append(int(b))

if "5" in a:
    big_a = a.replace("5", "6")
    big.append(int(big_a))
else:
    big.append(int(a))

if "5" in b:
    big_b = b.replace("5", "6")
    big.append(int(big_b))
else:
    big.append(int(b))

print(sum(small), sum(big))





