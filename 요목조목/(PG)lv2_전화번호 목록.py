# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]
answer = True
dic = {}

for x in phone_book:
    dic[x] = 1
print(dic)

for check in phone_book:
    num = ""
    for y in check:
        num += y
        print(num, check)
        print(num in dic, num != check)
        if num in dic and num != check:
            answer = False
            break
    if answer == False:
        break
print(answer)



