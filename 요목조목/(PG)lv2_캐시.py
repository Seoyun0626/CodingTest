# catchsize = 2
# cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
# catchsize = 5
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
# catchsize = 0
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# print(cities)
time = 0
stack = []


if catchsize == 0:
    time = len(cities) * 5
else:
    for x in cities:
        x = x.lower()
        if x not in stack:
            time += 5
            if len(stack) >= catchsize:
                stack.pop(0)
            stack.append(x)
        else:
            time += 1
            x_index = stack.index(x)
            stack.pop(x_index)
            stack.append(x)
        # print(stack, time)
print(time)

