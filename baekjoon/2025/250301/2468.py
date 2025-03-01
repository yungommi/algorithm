#예상 시간복잡도 O(N^2)

import sys
input = sys.stdin.readline

N = int(input())
min_ = 100
max_ = 1
world = [[] for _ in range(N)]
for _ in range(N):
    tmp = list(map(int, input().split()))
    min_ = min(min_, min(tmp))
    max_ = max(max_, max(tmp))
    world[_] = tmp
#print(world)
#print(min_, max_)

def dfs(i,j):
    stack = [(i,j)]
    visited.add((i,j))
    size = 1 
    while stack:
        x,y = stack.pop()
        for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and world[nx][ny]>val and (nx,ny) not in visited:
                visited.add((nx,ny))
                stack.append((nx,ny))

ans = 1
for val in range(min_, max_):
    visited = set()
    tmp = 0 
    for i in range(N):
        for j in range(N):
            if world[i][j] > val and (i,j) not in visited:
                tmp += 1 
                dfs(i,j)
    ans = max(ans, tmp)

print(ans)
    
