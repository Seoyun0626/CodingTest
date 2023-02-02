def solution(new_id):
    import string
    check_option = ["-", "_", "."]
    id_1 = new_id


    id_1 = id_1.lower()
    # print(id_1)

    for x in id_1:
        if x not in string.punctuation:
            continue
        else:
            if x not in check_option:
                id_1 = id_1.replace(x, "")

    # print(id_1)

    while '..' in id_1:
        id_1 = id_1.replace('..','.')


    # print(id_1)

    if len(id_1) == 1:
        if id_1[0] == ".":
            id_1 = ""
    elif len(id_1) >= 2:
        if id_1[0] == ".":
            id_1 = id_1[1:]
        if id_1[-1] == ".":
            id_1 = id_1[:-1]
    else:
        id_i = ""

    # print(id_1)


    if len(id_1) == 0:
        id_1 += "a"


    if len(id_1) >= 16:
        id_1 = id_1[ :15]
        if id_1[-1] == ".":
            id_1 = id_1[:-1]

    # print(id_1)

    if len(id_1) <= 2:
        while len(id_1) < 3:
            id_1 += id_1[-1]

    return id_1