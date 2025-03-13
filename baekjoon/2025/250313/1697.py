#예상시간복잡도 : O(N) 

import sys
input = sys.stdin.readline
from collections import deque 

A,B = map(int, input().split())

queue = deque()
queue.append(A) 

visited = [0]*100005

while queue:
    now = queue.popleft()

    if now == B:
        print(visited[now])
        break

    for next in (now - 1, now + 1, now * 2):
        if 0<=next<=100000 and visited[next]==0:
            visited[next] = visited[now]+1
            queue.append(next)
        
