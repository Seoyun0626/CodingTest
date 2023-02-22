word = input()
cnt = 0
dic = {'c=' : 'č', 'c-' : 'ć', 'dz=' : 'dž', 'd-' : 'đ', 'lj' : 'lj', 'nj' : 'nj', 's=' : 'š', 'z=' : 'ž'}
i = 0
while i != len(word):
    tmp1 = word[i:i+2]
    tmp2 = word[i:i+3]
    if tmp1 in dic:
        i += 2
        cnt += 1
    elif tmp2 in dic:
        i += 3
        cnt +=1
    else:
        i += 1
        cnt += 1
print(cnt)


