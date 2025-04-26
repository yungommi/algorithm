#예상시간복잡도 : O(N^2)

import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
dp1 = [1]*N 
for i in range(1,N):
    for j in range(i):
        if l[j] < l[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)
dp2 = [0]*N 
for i in range(N-2,-1,-1):
    for j in range(N-1,i,-1):
        if l[j] < l[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)
ans = 0  
for i in range(N):
    ans = max(ans, dp1[i]+dp2[i])
print(ans)

