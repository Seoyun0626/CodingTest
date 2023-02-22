def solution(today, terms, privacies):
    # 모든 달이 28일 이므로 날짜를 일로 변경하여 풀기

    # today = "2022.02.28"
    # terms = ["A 23"]
    # privacies = ["2020.01.28 A"]
    # today = "2022.05.19"
    # terms = ["A 6", "B 12", "C 3"]
    # privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    # today = "2020.01.01"
    # terms = ["Z 3", "D 5"]
    # privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    result = []
    privacies_dic = {}
    today_day = 0
    terms_dic = {}


    year, month, day = map(int, today.split("."))
    today_day += year * 28 * 12
    today_day += month * 28
    today_day += day
    today_day
    # print(today_day)


    for i in range(len(terms)):
        kind, month = map(str, terms[i].split())
        terms_dic[kind] = int(month) * 28
    # print(terms_dic)

    for i in range(len(privacies)):
        tmp = 0
        date, kind = privacies[i].split()
        year, month, day = map(int, date.split("."))
        tmp += year * 12 * 28
        tmp += month * 28
        tmp += day
        privacies_dic[tmp] = kind
    # print(privacies_dic)


    for i, (day, kind) in enumerate(privacies_dic.items()):
        # print(day, kind, day + terms_dic[kind], today_day)
        if (day + terms_dic[kind] - 1) < today_day:
            result.append(i + 1)

    return result