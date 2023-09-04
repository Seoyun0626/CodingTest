def solution(genres, plays):
    dic = {} #장르 + 횟수
    total_play = {} # 장르별 총 재생횟수
    answer = []

    # genres = ["classic", "pop", "classic", "classic", "pop"]
    # plays = [500, 600, 150, 800, 2500]
    for i in range (len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in dic.keys():
            dic[genre] = [(play, i)]
            total_play[genre] = play
        else:
            total_play[genre] += play
            dic[genre].append((play, i))
    # print(dic)
    # print(total_play)

    total_play = sorted(total_play.items(), key = lambda x : x[1], reverse=True)
    print(total_play)

    for key in total_play:
        playlist = dic[key[0]]
        playlist = sorted(playlist, key = lambda x : x[0], reverse = True)
        # print(playlist)
        if len(playlist) == 1:
            answer.append(playlist[0][1])
        else:
            for i in range(2):
                answer.append(playlist[i][1])
    return answer