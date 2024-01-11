def solution(number, limit, power):
    answer = 0
    cnt_list = []
    for i in range(1, number+1):
        count = cnt(i)
        if count <= limit:
            cnt_list.append(count)
        else:
            cnt_list.append(power)
    answer = sum(cnt_list)
    return answer

def cnt(num):
    count = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count += 1
    if num == 1:
        count = 1
    elif ((num**(1/2)) == int(num**0.5)):
        count = 2*(count-1)+1
    else:
        count = 2*count
    return count