# 예상 시간복잡도: O(N)

def solution(d, budget):
    d.sort()
    sum = 0
    for i, x in enumerate(d):
        if sum + x <= budget:
            sum += x 
        else:
            return i
    return i+1


