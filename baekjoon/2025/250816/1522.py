#예상시간복잡도 : O(1000000)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


dp = [0]*1000001 
dp[1]=1
dp[2]=2
dp[3]=4 
for i in range(4, 1000001):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    dp[i] %= 1000000009

n = int(input())
for i in range(n):
    print(dp[int(input())]) 

'''def function(k):
    if dp[k]==0:
        dp[k]=function(k-1)+function(k-2)+function(k-3)
    return dp[k]


for i in range(n):
    print(function(int(input()))) 
'''