#예상시간복잡도 : O(N^2) 

import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int,input().split()))
dp = [0]*n
dp[0]=1

for i in range(1,n):
    now = list[i]
    ref = 1
    for j in range(i):
        if list[j]>now :
            ref = max(ref,dp[j]+1)
    dp[i]=ref 
print(max(dp))
