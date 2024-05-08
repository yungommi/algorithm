# 예상 시간복잡도: O(n)

def solution(n):
    ans = 0
    for i in range(n):
        ans += 1
        while ans%3 == 0 or '3' in str(ans):
            ans += 1
    return ans


