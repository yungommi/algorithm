# 예상 시간복잡도: O(N^2)

def solution(k, score):
    answer = []
    tmp = []
    for x in score: 
        tmp.append(x)
        tmp.sort(reverse=True)
        tmp = tmp[:k]
        answer.append(tmp[-1])     
    return answer

