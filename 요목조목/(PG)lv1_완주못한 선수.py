#정확도와 효율성 둘다 잡은 함수
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)


    for p, c in zip(participant, completion):
        print(p, c)
        if p != c:
            return p

    return participant[-1]
print(solution(participant, completion))
















#정확도는 좋지만 효율성은 떨어지는 함수


# dic = {value: index for index, value in enumerate(participant)}
# for key, value in dic.items():
#     for x in completion:
#         if key == x:
#             participant.remove(x)
#
#
# print(*participant)

#정확도와 효율성 둘다 잡은 함수

