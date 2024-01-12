# 예상 시간복잡도: O(logN)

def solution(a, b, n):
    ans = 0
    while n>= a:
        x,y = divmod(n,a)
        ans += x*b
        n = x*b +y 
    return ans


