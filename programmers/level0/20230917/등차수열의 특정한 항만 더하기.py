# 예상 시간복잡도 : O(n) 

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += (a+d*i)
    return answer

    
