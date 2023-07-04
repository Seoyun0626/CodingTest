def solution(operations):
    import heapq
    import sys

    input = sys.stdin.readline

    min_heap = []
    max_heap = []
    answer = []

    # operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    # operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

    for i in operations:
        op, num = i.split()
        if op == "I":
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
        if op == "D":
            if len(min_heap) != 0:
                if num == "-1":
                    min_num = heapq.heappop(min_heap)
                    max_heap.remove(-1 * min_num)

                else:
                    max_num = -1 * heapq.heappop(max_heap)
                    min_heap.remove(max_num)
    if len(min_heap) == 0:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(max(min_heap))
        answer.append(min(min_heap))
    # print(answer)
    return answer