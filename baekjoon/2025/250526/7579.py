#예상시간복잡도 : O(XY)
import sys
input = sys.stdin.readline

X = input().rstrip()
Y = input().rstrip() 
x_n = len(X)
y_n = len(Y)
dp = [[0]*(x_n+1) for _ in range(y_n+1)]

ans = 0 
for y in range(1,y_n+1):
    for x in range(1,x_n+1):
        if X[x-1]==Y[y-1]:
            dp[y][x]=dp[y-1][x-1]+1 
            ans = max(ans, dp[y][x])
print(ans)