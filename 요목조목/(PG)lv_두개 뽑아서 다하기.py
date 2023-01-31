numbers = [2,1,3,4,1]
answer = []
for x in numbers:
    for i in range(len(numbers)):
        if numbers.index(x) != i:
            answer.append(x + numbers[i])
answer = list(set(answer))
answer.sort()
print(answer)