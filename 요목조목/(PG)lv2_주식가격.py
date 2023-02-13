from collections import deque

prices = [1, 2, 3, 2, 3]
answer = []
queue = deque(prices)


while queue:
    price = queue.popleft()
    sec = 0
    for x in queue:
        sec += 1
        if price > x:
            break
    answer.append(sec)
print(answer)




# 시간 초과(정확성 통과, 효율성 실패)

# prices = [1, 2, 3, 2, 3]
# answer = []
# stack = []
# for i in range(len(prices)):
#     flag = 0
#     for j in range(i + 1, len(prices)):
#         # print(i, j)
#         # print(prices[i], prices[j])
#         if prices[i] <= prices[j]:
#             stack.append(prices[j])
#             # print(stack)
#         else:
#             flag = 1
#             answer.append(j - i)
#             stack = []
#             break
#     if flag == 0:
#         answer.append(j - i)
#         stack = []
# print(answer)



