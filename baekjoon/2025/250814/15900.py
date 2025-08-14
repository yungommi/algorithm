#예상시간복잡도 : O(N)
#계속틀림 ㅋㅋ ㅋ ㅋ

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
d = [[] for i in range(N + 1)]
for i in range(N-1):
    a,b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

arr = [0]*(N+1)
def function(n, prev, dep):
    for i in d[n]:
        if i != prev:
            arr[i] = dep + 1 
            function(i,n,dep+1)
    
function(1,0,0)

depth_sum = 0 

for i in range(2,N+1):
    if len(d[i])==1:
        depth_sum += arr[i] 


print("No") if depth_sum %2 == 0 else print("Yes")
