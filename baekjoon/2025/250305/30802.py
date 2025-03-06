#예상시간복잡도 : O(N)

import sys 
input = sys.stdin.readline 

N = int(input())
l = list(map(int,input().split()))
T,P = map(int,input().split())
ts = 0 
for x in l:
    if x%T==0:
        ts += x//T
    else:
        ts += (x//T + 1)
div, mod = divmod(N,P)
print(ts)
print(div,mod)
