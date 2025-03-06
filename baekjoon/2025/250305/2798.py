#예상시간복잡도 : O(N)

import sys 
input = sys.stdin.readline 
from itertools import combinations

N,M = map(int, input().split())
l = list(map(int,input().split()))
n = list(combinations(l,3))
#print(n)
ans = 0
for itm in n:
    s_ = sum(itm)
    #print(s_)
    if s_<=M:
        ans = max(s_,ans)

print(ans)

