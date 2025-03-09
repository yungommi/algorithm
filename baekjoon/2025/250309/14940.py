#예상시간복잡도 : O(N*M)

import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
orig = [[]]*N

for n in range(N):
    tmp = list(map(int,input().split()))
    orig[n] = tmp
    if 2 in tmp:
        m = tmp.index(2)
        t_n , t_m = n,m

#print(orig)
new = [[0]*M for _ in range(N)]

qu = deque()
qu.append((t_n,t_m))
step = 1
while qu:
    x,y = qu.popleft()
    for dx,dy in ([1,0],[0,1],[-1,0],[0,-1]):
        nx,ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M:
            if orig[nx][ny]==1 and new[nx][ny]==0:
                qu.append((nx,ny))
                new[nx][ny] = new[x][y]+1
for i in range(N):
    for j in range(M):
        if new[i][j]==0:
            if orig[i][j]==1:
                new[i][j]=-1

#print(new)
for l in new:
    print(" ".join(str(x) for x in l))

