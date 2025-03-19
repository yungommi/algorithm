#예상시간복잡도 : O(n C m )

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s = []
def dfs (start):
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    for i in range(start,N+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1) 