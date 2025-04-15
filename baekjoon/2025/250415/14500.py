#예상시간복잡도 : O(NM)
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(N)]
tetro = [[(0,1),(0,2),(0,3)], [(1,0),(2,0),(3,0)],
         [(1,0),(0,1),(1,1)],
         [(1,0),(2,0),(2,1)],[(1,0),(2,0),(2,-1)],[(1,0),(2,0),(0,1)],[(1,0),(2,0),(0,-1)],
         [(1,0),(1,1),(1,2)],[(1,-2),(1,-1),(1,0)],[(1,0),(0,1),(0,2)],[(0,1),(0,2),(1,2)],
         [(1,0),(1,1),(2,1)],[(1,0),(1,-1),(2,-1)],[(0,1),(-1,1),(-1,2)],[(0,1),(1,1),(1,2)],
         [(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)],[(0,1),(-1,1),(1,1)],[(0,-1),(-1,-1),(1,-1)]]

ans = 0 
for i in range(N):
    for j in range(M):
        for tet in tetro:
            tmp = table[i][j]
            for dx,dy in tet:
                nx,ny = i+dx, j+dy 
                if 0<=nx<N and 0<=ny<M:
                    tmp+= table[nx][ny]
                else:
                    break 
                ans = max(tmp,ans) 
print(ans)