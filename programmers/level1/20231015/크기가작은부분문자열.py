# 예상 시간복잡도: O(N)

def solution(t, p):
    ans = 0
    for i in range(0,len(t)-len(p)+1):
        tmp = int(t[i:i+len(p)])
        if tmp <= int(p):
            ans += 1
    return ans

