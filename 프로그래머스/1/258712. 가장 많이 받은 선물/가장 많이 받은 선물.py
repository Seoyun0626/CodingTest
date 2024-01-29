def solution(friends, gifts):
    answer = 0
    # 주고받은 선물 -> 2차원 배열
    present = [[0]*len(friends) for _ in range(len(friends))]
    give_take_index = []
    result = []
    dict = {}
    total_dict = {}
    for i in range(len(friends)):
        dict[friends[i]] = i
        total_dict[friends[i]] = 0
    # print(dict)
    # print(present)
    for gift in gifts:
        a,b = gift.split(" ")
        first = dict[a]
        second = dict[b]
        present[first][second] += 1
    # print(present)
    tmp_present = list(map(list, zip(*present)))
    for i in range(len(present)):
        give = sum(present[i])
        take = sum(tmp_present[i])
        index = give-take
        give_take_index.append((give,take,index))
    # print(give_take_index)
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                if present[i][j] > present[j][i]:
                    total_dict[friends[i]] += 1
                elif present[i][j] == present[j][i]:
                    a_index = give_take_index[i][2]
                    b_index = give_take_index[j][2]
                    if a_index > b_index:
                        total_dict[friends[i]] += 1
    values = total_dict.values()
    answer = max(values)
    return answer