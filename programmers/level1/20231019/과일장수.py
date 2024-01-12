# 예상 시간복잡도: O(N)

def solution(k, m, score):
    l = len(score)
    n = l // m
    score.sort(reverse=True)
    ans = 0 
    for i in range(n):
        ans += (score[i*m:(i+1)*m][-1])*m
    return ans