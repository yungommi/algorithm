#예상시간복잡도 : O(N^2)
'''
import sys
input = sys.stdin.readline
from math import inf

N,E = map(int,input().split())
dic = {i:[] for i in range(1,N+1)}
for _ in range(E):
    a,b,v = map(int,input().split())
    dic[a].append((b,v))
    dic[b].append((a,v))
v_1,v_2 = map(int,input().split())

def findsmallest (distance, visited):
    min_v = inf
    idx= -1
    for i in range(1,N+1):
        if distance[i]<min_v and not visited[i]:
            min_v = distance[i]
            idx = i 
    return idx

def dijk(start):
    visited = [False]*(N+1)
    distance = [inf]*(N+1)
    distance[start]=0
    for d,v in dic[start]:
        distance[d]=v 
    for _ in range(N-1):
        now= findsmallest(distance, visited)
        if now == -1:
            break
        visited[now]=True 
        for d,v in dic[now]:
            distance[d] = min(distance[d], distance[now]+v)
    return distance

D_st = dijk(1)
D_1 = dijk(v_1)
D_2 = dijk(v_2)

ans1 = D_st[v_1]+D_1[v_2]+D_2[N]
ans2 = D_st[v_2]+D_2[v_1]+D_1[N]
if min(ans1,ans2) >= inf:
    print(-1)
else:
    print(min(ans1,ans2))'''


import sys
import heapq
from math import inf
input = sys.stdin.readline

N, E = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijk(start):
    distance = [inf] * (N + 1)
    distance[start] = 0
    heap = [(0, start)]  
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue  
        for neighbor, cost in graph[now]:
            new_dist = dist + cost
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return distance
D_st = dijk(1)
D_1 = dijk(v1)
D_2 = dijk(v2)

ans1 = D_st[v1]+D_1[v2]+D_2[N]
ans2 = D_st[v2]+D_2[v1]+D_1[N]
if min(ans1,ans2) >= inf:
    print(-1)
else:
    print(min(ans1,ans2))