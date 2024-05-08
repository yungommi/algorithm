# 예상 시간복잡도: O(N)

import math 
def solution(n, m):
    return [math.gcd(m,n), m*n/math.gcd(m,n)]

