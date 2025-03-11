#예상시간복잡도 : O(N+i) NL노드 i:간선 

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
i = int(input())
d = {}
for _ in range(i):
    a,b = map(int, input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a]=[b]
    if b in d:
        d[b].append(a)
    else:
        d[b]=[a]

qu = deque()
if 1 in d:
    qu.extend(d[1]) #qu += d[1] 보다 빠르다~ 

ans = set()
ans.add(1)
while qu:
    x = qu.popleft()
    ans.add(x)
    if x in d:
        for itm in d[x]:
            if itm not in ans:
                qu.append(itm)

print(len(ans)-1)
