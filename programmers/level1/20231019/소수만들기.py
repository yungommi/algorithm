# 예상 시간복잡도: O(N)

from itertools import combinations
def solution(nums):
    ans = 0
    t = combinations(nums,3)
    t=list(t)
    for x in t:
        if isprime(sum(x)):
            ans += 1
    return ans

def isprime(n):
    for i in range(2,n):
        if n%i==0 :
            return False
    return True 