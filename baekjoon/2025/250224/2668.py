#예상 시간복잡도 O(N^2) 

import sys
input = sys.stdin.readline
N=int(input())

l = [0]*(N+1)
for i in range(1,N+1):
    x = int(input())
    l[i] = x

ans = []
def dfs(n):
    if visited[n]==False:
        visited[n]= True
        up.add(n)
        down.add(l[n])
        if up == down:
            ans.extend(list(down))
            return
        dfs(l[n])

for i in range(1,N+1):
    visited = [False]*(N+1)
    up = set()
    down = set()
    dfs(i)

ans = list(set(ans))
ans.sort()
n = len(ans)
print(n)
for x in ans:
    print(x)