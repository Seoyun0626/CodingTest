# 런타임에러

person1 = [1, 2, 3, 4, 5]
person2 = [2, 1, 2, 3, 2, 4, 2, 5]
person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
answers = [4]

an_person1 = []
an_person2 = []
an_person3 = []

cnt1 = 0
cnt2 = 0
cnt3 = 0
total = []
result = []

for i in range(len(answers)):
    an_person1.append(person1[i % len(person1)])
    an_person2.append(person2[i % len(person2)])
    an_person3.append(person3[i % len(person3)])


for i in range(len(answers)):
    if an_person1[i] == answers[i]:
        cnt1 += 1
    if an_person2[i] == answers[i]:
        cnt2 += 1
    if an_person3[i] == answers[i]:
        cnt3 += 1

big = max(cnt1, cnt2, cnt3)
if cnt1 == big:
    result.append(1)
if cnt2 == big:
    result.append(2)
if cnt3 == big:
    result.append(3)
print(result)



