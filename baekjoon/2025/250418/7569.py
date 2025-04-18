#예상시간복잡도 : O(NMH)
import sys
input = sys.stdin.readline
from collections import deque 

M,N,H = map(int,input().split())
tomato = [[list(map(int,input().split())) for n in range(N)] for h in range(H)]
day = [[[0]*M for n in range(N)] for h in range(H)]
q = deque() 
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m]==1:
                q.append((h,n,m))

while q:
    h,n,m = q.popleft()
    for dm,dn,dh in [[-1,0,0],[0,-1,0],[0,0,-1],[1,0,0],[0,1,0],[0,0,1]]:
        nm,nn,nh = m+dm, n+dn,h+dh 
        if 0<=nm<M and 0<=nn<N and 0<=nh<H:
            if tomato[nh][nn][nm]==0:
                day[nh][nn][nm] = day[h][n][m]+1 
                tomato[nh][nn][nm]=1 
                q.append((nh,nn,nm))

ans = 0  
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m]==0:
                print(-1)
                exit()
            ans = max(ans, day[h][n][m])
print(ans)
