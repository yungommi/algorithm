#예상시간복잡도 : O(N)

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
num = 1
q = deque([i for i in range(1,n+1)])
while len(q)>1:
    tmp = q.popleft()
    if num%2 == 1:
        pass
    else:
        q.append(tmp)
    num += 1 
print(q[0])
