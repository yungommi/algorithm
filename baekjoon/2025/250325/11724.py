#예상시간복잡도 : O(N+M)

import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
dict = {i:[] for i in range(1,N+1)}
for _ in range(M):
    u,v = map(int, input().split())
    dict[u].append(v)
    dict[v].append(u)

visited = set()
que = deque()
ans = 0 

for i in range(1,N+1):
    if i not in visited:
            que.append(i)
            ans += 1 
    while que:
        now = que.popleft()
        visited.add(now)
        for k in dict[now]:
              if k not in visited:
                    que.append(k)
                    visited.add(k)
print(ans)
