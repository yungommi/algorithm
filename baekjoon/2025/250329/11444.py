#예상시간복잡도 : O(log(N))

import sys
input = sys.stdin.readline

n = int(input())

dict = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5}

def function(n):
    if n in dict:
        return dict[n]
    else:
        m = n//2
        if n%2==0:
            ans = (function(m) * ( function(m) + 2 * function(m-1))) %1000000007
        else:
            ans = (function(m+1)**2 + function(m)**2)%1000000007
    dict[n]=ans
    return ans

print(function(n))
