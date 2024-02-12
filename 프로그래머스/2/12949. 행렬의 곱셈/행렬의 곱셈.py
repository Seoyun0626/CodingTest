def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    # print(answer)
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr1[0])):
                sum += (arr1[i][k] * arr2[k][j])
            answer[i].append(sum)
    return answer