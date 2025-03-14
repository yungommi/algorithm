#예상시간복잡도 : O(N) 

import sys
input = sys.stdin.readline

source = input().rstrip()
target = input().rstrip()
s = len(source)
t = len(target)

dp = [[0]*(t+1) for _ in range(s+1)]
for i in range(1,s+1):
    for j in range(1,t+1):
        if source[i-1]==target[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[s][t])

