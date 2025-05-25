#예상시간복잡도 : O(N)
import sys
input = sys.stdin.readline

ddr = list(map(int,input().split()))
N = len(ddr)
dp = [[[N*4 for _ in range(5)] for _ in range(5)] for _ in range(N)]
dp[0][0][0]=0

def calc(x,next):
    if x==0:
        return 2 
    tmp = abs(x-next)
    if tmp == 0 :
        return 1 
    elif tmp%2 ==1:
        return 3 
    else:
        return 4 
 
for i in range(N-1):
    target = ddr[i]
    for l in range(5):
        for r in range(5):
            dp[i+1][l][target]= min(dp[i+1][l][target], dp[i][l][r]+calc(r,target))
            dp[i+1][target][r]=min(dp[i+1][target][r], dp[i][l][r]+calc(l,target)) 
#print(dp[N-1])
ans = N*4
for x in dp[N-1]:
    for y in x:
        ans = min(y,ans)
print(ans)