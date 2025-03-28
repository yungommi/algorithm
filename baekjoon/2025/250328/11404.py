#예상시간복잡도 : O(N^3)

import sys
input = sys.stdin.readline
from math import inf 

n = int(input())
dp = [[inf]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][i]=0
bus = int(input())
for _ in range(bus):
    a,b,c = map(int,input().split())
    dp[a][b]=min(dp[a][b],c)

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            dp[a][b] = min(dp[a][b], dp[a][i]+dp[i][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if dp[i][j]==inf:
            dp[i][j] = 0 
    print(' '.join(map(str,dp[i][1:])))

