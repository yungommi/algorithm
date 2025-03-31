#예상시간복잡도 : O(N)

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)
parent = [0]*(n+1)

def bfs(start):
    q = deque([start])
    visited[start]= 1
    while q:
        now = q.popleft()
        for child in graph[now]:
            if visited[child]==0:
                parent[child]=now 
                visited[child]=1 
                q.append(child)

bfs(1)
for i in range(2,n+1):
    print(parent[i])
