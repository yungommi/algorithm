# 예상 시간 복잡도 O(len(arr))

from math import gcd  
def solution(arr):                         
    ans = 1                              
    for x in arr:                             
        ans = ans*x // gcd(ans, x)     
    return ans
