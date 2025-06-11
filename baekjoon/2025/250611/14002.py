#예상시간복잡도 : N^2
import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
dp = [1]*(N)

for i in range(N):
    for j in range(i):
        if l[j]<l[i]:
            dp[i] = max(dp[i], dp[j]+1)
x = max(dp)
print(x)
res = []
for i in range(N-1,-1,-1):
    if dp[i]==x:
        res.append(l[i])
        x -= 1 
res.reverse()
print(" ".join(map(str,res)))
