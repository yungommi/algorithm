#예상시간복잡도 : O(N^2)

import sys
input = sys.stdin.readline

N = int(input())

time = [list(map(int, input().split())) for i in range(N)]
dp = [0] * (N+1)

for i in range(N):
    for j in range(i+time[i][0], N+1):
        if dp[j]<dp[i]+time[i][1]:
            dp[j]=dp[i]+time[i][1]
print(dp[-1])