# DVD 용량의 최소 : 1(lt), DVD 용량의 최대 : 전체 합(rt)
# 내부에서 여러번 돌 때 res변수설정해서 결과 값 저장해놓고 있기

n, m = map(int, input().split())
music = list(map(int, input().split()))
lt = 1
rt = sum(music)

def check(mid):
    count = 0
    total = 0
    for x in music:
        total += x
        if total <= mid:
            continue
        else:
            total = 0
            count += 1
            total += x
    count += 1
    return count



while lt <= rt:
    mid = (lt + rt) // 2
    cnt = check(mid)
    # print(cnt,mid,lt,rt)
    if m >= cnt:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)