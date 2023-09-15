numbers = [1, 1, 1, 1, 1]
target = 3
answer = 0
result = 0

def dfs(i, result):
    if i == len(numbers):
        if result == target:
            nonlocal answer
            answer += 1
        else:
            return
    else:
        dfs(i + 1, result + numbers[i])
        dfs(i + 1, result - numbers[i])
dfs(0,0)
print(answer)