def solution(scoville, K):
    import heapq


    # scoville = [1, 2, 3, 9, 10, 12]
    heapq.heapify(scoville)
    # K = 7
    result = 0

    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        else:
            if len(scoville) == 0:
                result = -1
                break
            else:
                second = heapq.heappop(scoville)
                new = first + 2 * second
                heapq.heappush(scoville, new)
                result += 1
    return result