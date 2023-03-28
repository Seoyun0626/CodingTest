l = int(input())
height = list(map(int, input().split()))
m = int(input())
cnt = 0
info = {}
index = []

for i in range(1, l+1):
    info[i] = height[i-1]
# print(info)


def find_index():
    global info
    global index
    info = dict(sorted(info.items(), key = lambda x : x[1], reverse=True))
    # print(info)
    index = list(info.keys())
    return index


while cnt < m:
    cnt += 1
    find_index()
    high_index = index[0]
    low_index = index[-1]
    info[high_index] -= 1
    info[low_index] += 1
    # print(cnt, info)
result = list(info.values())
print(max(result) - min(result))