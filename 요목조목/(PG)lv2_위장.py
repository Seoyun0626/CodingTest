# 입거나 안 입거나
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
dic = {}
answer = 1


for item, category in clothes:
    if category not in dic:
        dic[category] = 1
    else:
        dic[category] += 1

for key, value in dic.items():
    answer *= (value + 1)
answer -= 1

print(answer)