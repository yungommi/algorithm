#예상시간복잡도 : O(N+M)
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
jump = {}
board = [0]*101
visited = [False]*101 
for i in range(n+m):
    x,y = map(int, input().split())
    jump[x]=y
q = deque()
q.append(1)
visited[1]=True 
while q:
    cur = q.popleft() 
    tmp = board[cur]
    for i in range(1,7):
        next = cur + i 
        if next <=0 or next>100:
            continue
        if visited[next]==False:
            visited[next]=True
            board[next]=tmp+1 
            if next in jump.keys():
                next = jump[next]
                if visited[next]==False:
                    visited[next]=True
                    board[next]=tmp+1 
                    q.append(next)
            else:
                q.append(next)
            
print(board[100])
