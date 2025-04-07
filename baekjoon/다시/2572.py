#예상시간복잡도 : O(MN)

import sys
input = sys.stdin.readline

N = int(input())
card = list(input().split())
M,K = map(int,input().split())
dic = {i:[] for i in range(1,M+1)}
for i in range(K):
    x,y,c = input().split()
    dic[int(x)].append((int(y),c))
    dic[int(y)].append((int(x),c))
dp = [[-1]*(M+1) for _ in range(N+1)]
dp[0][1] = 0 
for i in range(N):
    for j in range(1,M+1):
        if dp[i][j]==-1:
            continue
        for x,c in dic[j]:
            if c == card[i]:
                dp[i+1][x] = max(dp[i+1][x], dp[i][j]+1)
            else:
                dp[i+1][x] = max(dp[i+1][x], dp[i][j])

ans = max(dp[N])
print(ans * 10 if ans != -1 else 0)
