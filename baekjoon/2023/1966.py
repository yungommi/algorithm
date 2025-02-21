# 1966
from collections import deque
n = int(input())
for i in range(n):
    k,idx = map(int,input().split())
    q = deque(list(map(int, input().split())))
    ans = 0
    while q:
        max_v = max(q)
        tmp = q.popleft()
        idx -= 1

        if max_v == tmp:
            ans += 1
            if idx < 0:
                print(ans)
                break
        else:
            q.append(tmp)
            if idx<0:
                idx = len(q)-1


