# 예상 시간복잡도: O(N)

def solution(n):
    ans = 0
    for x in str(n):
        ans += int(x)
    return ans

