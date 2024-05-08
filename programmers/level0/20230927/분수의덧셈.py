# 예상 시간복잡도: O(1)

import math
def solution(numer1, denom1, numer2, denom2):
    numer1 *= denom2
    numer2 *= denom1
    denom = denom1 * denom2
    numer = numer1 + numer2
    return [int(numer / math.gcd(numer,denom)) , int(denom/math.gcd(numer,denom))]

