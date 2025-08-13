#예상시간복잡도 : O(N * T)
import sys
input = sys.stdin.readline

T = int(input())

def function(N,l,target):
    dp = [[0]*(target+1) for _ in range(N+1)]
    dp[1][0] = 1
    for i in range(1,N+1):
        dp[i][0]=1
        x = l[i-1] 
        for k in range(1,target+1):
            dp[i][k]= dp[i-1][k] 
            if k >= x:
                dp[i][k] += dp[i][k-x]
    #print(dp)
    return dp[N][target]

for _ in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    target = int(input())
    print(function(N,l,target))