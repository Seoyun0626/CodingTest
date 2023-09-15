def solution(answers):
    # answers = [1,2,3,4,5]
    # answers = [1,3,2,4,2]

    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    an_person1 = []
    an_person2 = []
    an_person3 = []

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    result = []

    for i in range(len(answers)):
        num = answers[i]
        if person1[i%len(person1)] == num:
            cnt1 += 1
        if person2[i%len(person2)] == num:
            cnt2 += 1
            # print(i, num, person2[i])
        if person3[i%len(person3)] == num:
            cnt3 += 1
        # print(cnt1, cnt2, cnt3)

    big = max(cnt1, cnt2, cnt3)

    if cnt1 == big:
        result.append(1)
    if cnt2 == big:
        result.append(2)
    if cnt3 == big:
        result.append(3)
    return result