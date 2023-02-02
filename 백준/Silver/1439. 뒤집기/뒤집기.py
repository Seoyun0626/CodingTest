S = input()
new_s = ""
cnt1 = 1
cnt2 = 1
flag = 0
i = 0
result = 0
zero_cnt = 0
one_cnt = 0

while i + 1 < len(S):
    num = S[i]
    if S[i] != S[i + 1]:
        if flag == 0:
            new_s += S[i]
            new_s += S[i + 1]
            flag = 1
        else:
            new_s += S[i + 1]
    i += 1
if len(new_s) == 0:
    new_s += S[0]

for x in new_s:
    if x == "0":
        zero_cnt += 1
    else:
        one_cnt += 1

print(min(zero_cnt, one_cnt))








