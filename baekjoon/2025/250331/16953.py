#예상시간복잡도 : O(N)

import sys
input = sys.stdin.readline
from collections import deque

A,B = map(int,input().split())
def function(A,B):
    q = deque([(A,1)])
    while q:
        now,step = q.popleft()
        for tmp in [now*2, 10*now+1]:
            if tmp == B:
                return step+1
            if tmp<B:
                q.append((tmp,step+1))
    return -1 

print(function(A,B))
