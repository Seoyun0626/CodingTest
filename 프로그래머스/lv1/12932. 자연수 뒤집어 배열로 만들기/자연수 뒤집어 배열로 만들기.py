def solution(n):
    n = str(n)
    answer = []
    
    for i in n:
        answer.append(int(i))
    answer = answer[::-1]
        
    return answer