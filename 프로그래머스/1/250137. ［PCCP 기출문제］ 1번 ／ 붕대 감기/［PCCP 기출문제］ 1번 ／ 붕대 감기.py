def solution(bandage, health, attacks):
    bonus = bandage[1]+bandage[2]
    max_health = health
    index = 0
    now = 0
    for time, minus in attacks:
        double = 0
        check = 1
        time = time-now-1
        print("time", time)
        for i in range(time):
            print("check", check)
            # 보너스 치료 아닐 때
            if check != bandage[0]:
                check += 1
                health += bandage[1]
                print("no bonus health", health)
            # 보너스 치료 일 때
            else:
                check = 1
                health += bonus
                print("bonus",bonus)
                print("bouns health", health)
            # 최대 체력 넘어가는 경우
            if health > max_health:
                health = max_health
            now += 1
        now += 1
        health -= attacks[index][1]
        print("after monster","heatlh",health,"now", now)
        index += 1
        if health <= 0:
            return -1
    return health