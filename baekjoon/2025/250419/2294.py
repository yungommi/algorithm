#예상시간복잡도 : O(NMH)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

li =[]

for i in range(n):
   li.append(int(input().rstrip()))

dp = [10001] * (k+1)
dp[0] = 0

for num in li:
   for i in range(num, k+1):
       dp[i] = min(dp[i],dp[i-num]+1)
if dp[k] == 10001:
   print(-1)
else:
   print(dp[k])