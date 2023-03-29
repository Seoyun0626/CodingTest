# 강의 참고
# 그리디 핵심 : 정렬 -> 회의실 끝나는 시간 기준

n = int(input())
info = []
for _ in range(n):
    start, end = map(int, input().split())
    info.append((start,end))
info = sorted(info, key = lambda x : x[1])
# print(info)



start, end = info[0][0], info[0][1]
cnt = 1
for i in range(1,len(info)):
    if info[i][0] >= end:
        cnt += 1
        end = info[i][1]
print(cnt)

