#예상시간복잡도 : O(N)

import sys
input = sys.stdin.readline

n = int(input())

l = [0]*(41)
l[0] = [1,0]
l[1] = [0,1]
def function(N):
    if l[N]== 0:
        x = function(N-1)
        y = function(N-2)
        l[N] = [x[0]+y[0],x[1]+y[1]]
    return l[N] 

for _ in range(n):
    a= function(int(input()))
    print(a[0],a[1]) 

