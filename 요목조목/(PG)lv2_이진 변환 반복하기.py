# s = "110010101001"
# s = "0111010"
# s = "01110"
# s ="1111111"
result = []
cnt = 0
zero_cnt = 0
while True:
    if s != "1":
        cnt += 1
        tmp = len(s)
        s = s.replace("0","")
        zero_cnt += (tmp - len(s))
        tmp_num = len(s)
        s = ''
        while tmp_num != 0:
            s += str(tmp_num % 2)
            tmp_num = tmp_num // 2
        # print(cnt, zero_cnt, s)
    else:
        break
result.append(cnt)
result.append(zero_cnt)
print(result)








