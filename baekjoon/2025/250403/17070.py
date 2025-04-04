#예상시간복잡도 : O(N^2)

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0,0,0]for _ in range(n)] for _ in range(n)]
dp[0][1][0]=1
for i in range(2,n):
    if graph[0][i]==0:
        dp[0][i][0]=dp[0][i-1][0]

for i in range(1,n):
    for j in range(1,n):
        if graph[i][j]==0:
            if graph[i][j-1]==0:
                dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][1]
            if graph[i-1][j]==0:
                dp[i][j][2]=dp[i-1][j][1]+dp[i-1][j][2] 
            if graph[i-1][j-1]==0 and graph[i][j-1]==0 and graph[i-1][j]==0:
                dp[i][j][1]=dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))

