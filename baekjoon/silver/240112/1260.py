'''https://www.acmicpc.net/problem/1260'''
'''
import sys
input = sys.stdin.readline
from collections import deque


def bfs(grp, V):
    q = deque()
    q.append(V)
    done = [V]
    while q:
        tmp = q.popleft()
        for itm in grp[tmp]:
            if itm not in done:
                q.append(itm)
                done.append(itm)
    for k in done:
        print(k, end = ' ')

def dfs(grp, V):
    stack=[V]
    done = [V]
    while stack:
        tmp = stack.pop()
        for itm in grp[tmp]:
            if itm not in done:
                stack.append(itm)
                done.append(itm)
                break
    for k in done:
        print(k, end = ' ')

N,M,V = map(int, input().split())
grp = {}
for _ in range(M):
    x,y = map(int, input().split())
    if x in grp:
        grp[x].append(y)
    else:
        grp[x]=[y]
    if y in grp:
        grp[y].append(x)
    else:
        grp[y]=[x]
for _ in grp:
    grp[_] = sorted(grp[_])


dfs(grp,V)
print()
bfs(grp,V)'''

from collections import deque
n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for j in graph[v]:
        if not visited[j]:
            dfs(graph, j, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for k in graph[v]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True
                
visited = [False] * (n+1)        
dfs(graph, v, visited)
print()
visited = [False] * (n+1)  
bfs(graph, v, visited)

