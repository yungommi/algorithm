#예상시간복잡도 : O(N*K)

import sys 
input = sys.stdin.readline 

N,K = map(int,input().split())
dp = [0]*(K+1)
for _ in range(N):
    w,v = map(int,input().split())
    for i in range(K,w-1,-1):
        dp[i]=max(dp[i-w]+v,dp[i])
print(dp[K])
