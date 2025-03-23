#예상시간복잡도 : O(N) 

import sys
input = sys.stdin.readline

n = int(input())
table = [0]*(n+1)
for i in range(n):
    tmp = list(map(int,input().split()))
    table[i+1] = tmp

dp = [[0,0,0] for i in range(n+1)] 

for i in range(1,n+1):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+table[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+table[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1])+table[i][2]


print(min(dp[n]))

