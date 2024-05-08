# 예상 시간복잡도: O(n)

import math

def solution(arr):
    l = len(arr)
    if l==1:
        return arr
    n_ = int(math.log2(l-1))+1
    if n_ == 0 :
        return arr
    else:
        return arr + [0]*((2**n_)-l)
    
