#예상시간복잡도 : O(NlogN)
import sys
input = sys.stdin.readline

T = int(input())

def function(N,l,target):
    dp = [[0]*(target+1) for _ in range(N+1)]
    dp[1][0] = 1
    for k in range(1, target+1):
        x = l[0]
        if k%x == 0:
            dp[1][k] = 1 
    for i in range(1,N):
        dp[i+1][0]=1
        x = l[i] 
        for k in range(1,target+1):
            dp[i+1][k]= dp[i][k] 
            if k >= x:
                dp[i+1][k] += dp[i+1][k-x]
    #print(dp)
    return dp[N][target]

for _ in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    target = int(input())
    print(function(N,l,target))