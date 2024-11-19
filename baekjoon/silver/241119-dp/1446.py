#예상 시간복잡도 O(nlogn/ n: d) 

import sys
input = sys.stdin.readline

n, d = map(int, input().split())
dp = [i for i in range(d+1)]
shortcut=[]
for i in range(n):
    start, end, length = map(int, input().split())
    if end <= d and end-start > length:
        shortcut.append((start, end, length))

shortcut.sort()

for start, end, length in shortcut:
    if dp[end]>dp[start]+length:
        dp[end] = dp[start]+length
        for i in range(end+1, d+1):
            dp[i]=min(dp[i], dp[i-1]+1) 
            #처음에 이거 생각못함 / (0,80,20) (20,50,20)의 경우에 20:20 50:40 79:69 80:20  
    else:
        pass

print(dp[d])